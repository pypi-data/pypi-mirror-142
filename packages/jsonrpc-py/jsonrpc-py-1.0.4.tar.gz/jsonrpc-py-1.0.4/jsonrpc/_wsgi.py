# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
from binascii import b2a_base64 as b64encode
from collections.abc import Callable, Iterator, MutableMapping, MutableSequence
from functools import partial
from hashlib import md5
from http import HTTPStatus
from io import DEFAULT_BUFFER_SIZE, BytesIO
from traceback import print_exception
from typing import Any, ClassVar, Final, TypeAlias

from ._dispatcher import BaseDispatcher, Dispatcher
from ._errors import BaseError
from ._request import BaseBatchRequest, BaseRequest, BatchRequest, Request
from ._response import BaseBatchResponse, BaseResponse, BatchResponse, Response
from ._serializer import BaseSerializer, JSONSerializer
from ._typing import ExcInfo, Headers, InputStream, StartResponse, WSGIEnvironment

__all__: Final[tuple[str, ...]] = (
    "BaseWSGIHandler",
    "WSGIHandler"
)

_RequestBody: TypeAlias = MutableMapping[str, Any] | MutableSequence[MutableMapping[str, Any]]
_AnyRequest: TypeAlias = BaseRequest | BaseError | BaseBatchRequest
_AnyResponse: TypeAlias = BaseResponse | BaseBatchResponse | None


class BaseWSGIHandler(MutableMapping[str, Any], metaclass=ABCMeta):
    __slots__: tuple[str, ...] = "dispatcher", "serializer", "options"

    def __init__(self, *, dispatcher: BaseDispatcher, serializer: BaseSerializer, **options: Any) -> None:
        self.dispatcher: BaseDispatcher = dispatcher
        self.serializer: BaseSerializer = serializer
        self.options: dict[str, Any] = options

    def __getitem__(self, key: str, /) -> Any:
        return self.options[key]

    def __setitem__(self, key: str, value: Any, /) -> None:
        self.options[key] = value

    def __delitem__(self, key: str, /) -> None:
        del self.options[key]

    def __len__(self) -> int:
        return len(self.options)

    def __iter__(self) -> Iterator[str]:
        return iter(self.options)

    def __contains__(self, obj: Any, /) -> bool:
        return obj in self.options

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse, /) -> Iterator[bytes]:
        # Prevents the "start_response" argument duplicate invocation:
        wsgi_response: partial[Iterator[bytes]] = partial(self._get_response, start_response)

        if environ["REQUEST_METHOD"] not in self._allowed_methods:
            # Specified request method is invalid:
            return wsgi_response(status=HTTPStatus.METHOD_NOT_ALLOWED)

        try:
            if not (request_body := self._read_request_body(environ)):
                # Trying to check the request body is empty.
                # If that's true then it returns HTTP 400 "Bad Request".
                return wsgi_response(status=HTTPStatus.BAD_REQUEST)

            if not (response_body := self.process_request(request_body)):
                # Trying to check the response is empty.
                # If that's true then it returns empty response body.
                return wsgi_response(status=HTTPStatus.NO_CONTENT)

            # We're on a roll, baby. Send the response as is.
            return wsgi_response(response_body=response_body)

        except Exception as exc:
            # Houston, we have a problem O_o
            # In unexpected situations it raises the exception to WSGI server.
            print_exception(exc, file=environ["wsgi.errors"])
            exc_info: Final[ExcInfo] = type(exc), exc, getattr(exc, "__traceback__")
            return wsgi_response(status=HTTPStatus.INTERNAL_SERVER_ERROR, exc_info=exc_info)

    @property
    def _allowed_methods(self) -> Iterator[str]:
        # We are using the "POST" verb for the generic JSON-RPC invocations:
        yield "POST"
        # And the "PUT" verb generally for the notifications,
        # but no one forbids using it for the generic invocations too:
        yield "PUT"

    def _read_request_body(self, environ: WSGIEnvironment, /) -> bytes:
        try:
            content_length: int = int(environ["CONTENT_LENGTH"])
        except (KeyError, ValueError):
            return b""

        stream: InputStream = environ["wsgi.input"]

        with BytesIO() as raw_buffer:
            # Ensure to disallow reading the stream more bytes
            # than specified by "Content-Length" header:
            while content_length > 0:
                if not (chunk := stream.read(min(content_length, DEFAULT_BUFFER_SIZE))):
                    raise EOFError(f"Client disconnected, {content_length:d} more bytes were expected")

                # Appends the chunk of request body to the buffer
                # and decreases the request size:
                content_length -= raw_buffer.write(chunk)

            return raw_buffer.getvalue()

    def _md5_base64_digest(self, payload: bytes, /) -> str:
        md5_digest: Final[bytes] = md5(payload).digest()
        return b64encode(md5_digest, newline=False).decode("ascii")

    def _get_response(self,
        start_response: StartResponse,
        *,
        status: HTTPStatus = HTTPStatus.OK,
        response_body: bytes | None = None,
        media_type: str = "application/json",
        exc_info: ExcInfo | None = None
    ) -> Iterator[bytes]:
        content_length: int = len(response_body := b"" if response_body is None else response_body)
        headers: Headers = [
            ("Content-Length", f"{content_length:d}"),
            ("Content-MD5", self._md5_base64_digest(response_body))
        ]

        if content_length:
            # If the response body is empty,
            # we can omit passing the "Content-Type" header value,
            # elsewise it must be specified:
            headers.append(("Content-Type", media_type))

        start_response(f"{status.value:d}\x20{status.phrase!s}", headers, exc_info)
        yield response_body

    @abstractmethod
    def handle_request(self, obj: _AnyRequest, /) -> _AnyResponse:
        raise NotImplementedError

    @abstractmethod
    def process_request(self, request_body: bytes, /) -> bytes:
        raise NotImplementedError


class WSGIHandler(BaseWSGIHandler):
    """
    Base class representing the ``WSGI`` entry point.
    Its subclassing the :py:class:`collections.abc.MutableMapping` object
    for providing the user-defined data storage.

    For example::

        >>> app = WSGIHandler()
        >>> app["my_private_key"] = "foobar"
        >>> app["my_private_key"]
        "foobar"

    :var dispatcher: Instance variable representing the :class:`jsonrpc.Dispatcher` object
        used by this class for routing user-defined functions by default.
    :var serializer: Instance variable representing the :class:`jsonrpc.JSONSerializer` object
        used by this class for data serialization by default.
    :var options: Instance variable representing the :py:class:`dict` object
        for proxying the :py:class:`collections.abc.MutableMapping` interface methods.
    """
    __slots__: tuple[str, ...] = ()

    #: Class variable representing
    #: the default :class:`jsonrpc.Request` object implementation
    _request_cls: ClassVar[type[BaseRequest]] = Request

    #: Class variable representing
    #: the default :class:`jsonrpc.BatchRequest` object implementation
    _batch_request_cls: ClassVar[type[BaseBatchRequest]] = BatchRequest

    #: Class variable representing
    #: the default :class:`jsonrpc.Response` object implementation
    _response_cls: ClassVar[type[BaseResponse]] = Response

    #: Class variable representing
    #: the default :class:`jsonrpc.BatchResponse` object implementation
    _batch_response_cls: ClassVar[type[BaseBatchResponse]] = BatchResponse

    def __init__(self) -> None:
        super(WSGIHandler, self).__init__(dispatcher=Dispatcher(), serializer=JSONSerializer())

    def __repr__(self) -> str:
        return f"<{__package__}.{self.__class__.__name__}()>"

    def handle_request(self, obj: _AnyRequest, /) -> _AnyResponse:
        """
        Base method for handling deserialized requests.

        :param obj: One of the following objects types: :class:`jsonrpc.Request`, :class:`jsonrpc.Error` or :class:`jsonrpc.BatchRequest`.
            If the :class:`jsonrpc.BatchRequest` object type was supplied, its will be invoked itself recursively for each one
            item containing in the batch request.
        :returns: Either :class:`jsonrpc.Response` or :class:`jsonrpc.BatchResponse`.
            If the :class:`jsonrpc.Request` object was received and it's the notification returns :py:data:`None`.
        """
        if isinstance(obj, self._batch_request_cls):
            # We need to go deeper, 'cause received a batch request object.
            # Then invoke itself recursively.
            filterer: Final[Callable[[_AnyResponse], bool]] = lambda item: isinstance(item, self._response_cls)
            return self._batch_response_cls(filter(filterer, map(self.handle_request, obj)))

        if isinstance(obj, BaseError):
            # Returns the response as is with the error attribute.
            return self._response_cls(error=obj, response_id=None)

        if isinstance(obj, self._request_cls):
            # Trying to send the method to a dispatcher.
            # Returns the erroneous response if an exception is raised, otherwise the successful response.
            try:
                result: Any = self.dispatcher.dispatch(obj.method, *obj.args, **obj.kwargs)
                return self._response_cls(body=result, response_id=obj.request_id) if not obj.is_notification else None
            except BaseError as error:
                return self._response_cls(error=error, response_id=obj.request_id if not obj.is_notification else None)

    def process_request(self, request_body: bytes, /) -> bytes:
        """
        Base method for consuming a raw requests from ``WSGI`` server and producing the serialized responses.

        :param request_body: The :py:class:`bytes` object representing a request body incoming from ``WSGI`` server.
        :returns: The :py:class:`bytes` object representing a serialized response body for next sending to ``WSGI`` server.
        """
        try:
            obj: _RequestBody = self.serializer.deserialize(request_body)
        except BaseError as error:
            deserialization_error: BaseResponse = self._response_cls(error=error, response_id=None)
            return self.serializer.serialize(deserialization_error.json)

        is_batch_request: Final[bool] = isinstance(obj, MutableSequence) and len(obj) >= 1
        request: Final[_AnyRequest] = (self._batch_request_cls if is_batch_request else self._request_cls).from_json(obj)
        del is_batch_request

        if not (response := self.handle_request(request)):
            return b""

        try:
            return self.serializer.serialize(response.json)
        except BaseError as error:
            serialization_error: BaseResponse = self._response_cls(error=error, response_id=None)
            return self.serializer.serialize(serialization_error.json)
