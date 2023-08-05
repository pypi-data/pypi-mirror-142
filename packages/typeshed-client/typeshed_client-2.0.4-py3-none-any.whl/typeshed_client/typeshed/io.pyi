import builtins
import codecs
import sys
from _typeshed import ReadableBuffer, Self, StrOrBytesPath, WriteableBuffer
from os import _Opener
from types import TracebackType
from typing import IO, Any, BinaryIO, Callable, Iterable, Iterator, TextIO
from typing_extensions import Literal

if sys.version_info >= (3, 8):
    __all__ = [
        "BlockingIOError",
        "open",
        "open_code",
        "IOBase",
        "RawIOBase",
        "FileIO",
        "BytesIO",
        "StringIO",
        "BufferedIOBase",
        "BufferedReader",
        "BufferedWriter",
        "BufferedRWPair",
        "BufferedRandom",
        "TextIOBase",
        "TextIOWrapper",
        "UnsupportedOperation",
        "SEEK_SET",
        "SEEK_CUR",
        "SEEK_END",
    ]
else:
    __all__ = [
        "BlockingIOError",
        "open",
        "IOBase",
        "RawIOBase",
        "FileIO",
        "BytesIO",
        "StringIO",
        "BufferedIOBase",
        "BufferedReader",
        "BufferedWriter",
        "BufferedRWPair",
        "BufferedRandom",
        "TextIOBase",
        "TextIOWrapper",
        "UnsupportedOperation",
        "SEEK_SET",
        "SEEK_CUR",
        "SEEK_END",
    ]

DEFAULT_BUFFER_SIZE: Literal[8192]

SEEK_SET: Literal[0]
SEEK_CUR: Literal[1]
SEEK_END: Literal[2]

open = builtins.open

if sys.version_info >= (3, 8):
    def open_code(path: str) -> IO[bytes]: ...

BlockingIOError = builtins.BlockingIOError

class UnsupportedOperation(OSError, ValueError): ...

class IOBase:
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    read: Callable[..., Any]
    def readlines(self, __hint: int = ...) -> list[bytes]: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, __size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    write: Callable[..., Any]
    def writelines(self, __lines: Iterable[ReadableBuffer]) -> None: ...
    def readline(self, __size: int | None = ...) -> bytes: ...
    def __del__(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self, msg: str | None = ...) -> None: ...  # undocumented

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    def readinto(self, __buffer: WriteableBuffer) -> int | None: ...
    def write(self, __b: ReadableBuffer) -> int | None: ...
    def read(self, __size: int = ...) -> bytes | None: ...

class BufferedIOBase(IOBase):
    raw: RawIOBase  # This is not part of the BufferedIOBase API and may not exist on some implementations.
    def detach(self) -> RawIOBase: ...
    def readinto(self, __buffer: WriteableBuffer) -> int: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...
    def readinto1(self, __buffer: WriteableBuffer) -> int: ...
    def read(self, __size: int | None = ...) -> bytes: ...
    def read1(self, __size: int = ...) -> bytes: ...

class FileIO(RawIOBase, BinaryIO):  # type: ignore # argument disparities between the base classes
    mode: str
    name: StrOrBytesPath | int  # type: ignore[assignment]
    def __init__(
        self, file: StrOrBytesPath | int, mode: str = ..., closefd: bool = ..., opener: _Opener | None = ...
    ) -> None: ...
    @property
    def closefd(self) -> bool: ...
    def write(self, __b: ReadableBuffer) -> int: ...
    def read(self, __size: int = ...) -> bytes: ...
    def __enter__(self: Self) -> Self: ...

class BytesIO(BufferedIOBase, BinaryIO):  # type: ignore # argument disparities between the base classes
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    # BytesIO does not contain a "name" field. This workaround is necessary
    # to allow BytesIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def __enter__(self: Self) -> Self: ...
    def getvalue(self) -> bytes: ...
    def getbuffer(self) -> memoryview: ...
    if sys.version_info >= (3, 7):
        def read1(self, __size: int | None = ...) -> bytes: ...
    else:
        def read1(self, __size: int | None) -> bytes: ...  # type: ignore[override]

class BufferedReader(BufferedIOBase, BinaryIO):  # type: ignore # argument disparities between base classes
    def __enter__(self: Self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = ...) -> bytes: ...
    if sys.version_info >= (3, 7):
        def read1(self, __size: int = ...) -> bytes: ...
    else:
        def read1(self, __size: int) -> bytes: ...  # type: ignore[override]

class BufferedWriter(BufferedIOBase, BinaryIO):  # type: ignore # argument disparities between base classes
    def __enter__(self: Self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):
    def __enter__(self: Self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def seek(self, __target: int, __whence: int = ...) -> int: ...
    if sys.version_info >= (3, 7):
        def read1(self, __size: int = ...) -> bytes: ...
    else:
        def read1(self, __size: int) -> bytes: ...  # type: ignore[override]

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = ...) -> bytes: ...

class TextIOBase(IOBase):
    encoding: str
    errors: str | None
    newlines: str | tuple[str, ...] | None
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def detach(self) -> BinaryIO: ...
    def write(self, __s: str) -> int: ...
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = ...) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = ...) -> list[str]: ...  # type: ignore[override]
    def read(self, __size: int | None = ...) -> str: ...
    def tell(self) -> int: ...

class TextIOWrapper(TextIOBase, TextIO):  # type: ignore # argument disparities between base classes
    def __init__(
        self,
        buffer: IO[bytes],
        encoding: str | None = ...,
        errors: str | None = ...,
        newline: str | None = ...,
        line_buffering: bool = ...,
        write_through: bool = ...,
    ) -> None: ...
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def closed(self) -> bool: ...
    @property
    def line_buffering(self) -> bool: ...
    if sys.version_info >= (3, 7):
        @property
        def write_through(self) -> bool: ...
        def reconfigure(
            self,
            *,
            encoding: str | None = ...,
            errors: str | None = ...,
            newline: str | None = ...,
            line_buffering: bool | None = ...,
            write_through: bool | None = ...,
        ) -> None: ...
    # These are inherited from TextIOBase, but must exist in the stub to satisfy mypy.
    def __enter__(self: Self) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = ...) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = ...) -> list[str]: ...  # type: ignore[override]
    def seek(self, __cookie: int, __whence: int = ...) -> int: ...

class StringIO(TextIOWrapper):
    def __init__(self, initial_value: str | None = ..., newline: str | None = ...) -> None: ...
    # StringIO does not contain a "name" field. This workaround is necessary
    # to allow StringIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def getvalue(self) -> str: ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    def __init__(self, decoder: codecs.IncrementalDecoder | None, translate: bool, errors: str = ...) -> None: ...
    def decode(self, input: bytes | str, final: bool = ...) -> str: ...
    @property
    def newlines(self) -> str | tuple[str, ...] | None: ...
    def setstate(self, __state: tuple[bytes, int]) -> None: ...
