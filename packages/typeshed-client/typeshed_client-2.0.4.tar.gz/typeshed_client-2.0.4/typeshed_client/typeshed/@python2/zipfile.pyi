import io
from _typeshed import Self, StrPath
from types import TracebackType
from typing import IO, Any, Callable, Iterable, Pattern, Protocol, Sequence, Text, Union

_SZI = Union[Text, ZipInfo]
_DT = tuple[int, int, int, int, int, int]

class BadZipfile(Exception): ...

error = BadZipfile

class LargeZipFile(Exception): ...

class ZipExtFile(io.BufferedIOBase):
    MAX_N: int = ...
    MIN_READ_SIZE: int = ...

    PATTERN: Pattern[str] = ...

    newlines: list[bytes] | None
    mode: str
    name: str
    def __init__(
        self,
        fileobj: IO[bytes],
        mode: str,
        zipinfo: ZipInfo,
        decrypter: Callable[[Sequence[int]], bytes] | None = ...,
        close_fileobj: bool = ...,
    ) -> None: ...
    def read(self, n: int | None = ...) -> bytes: ...
    def readline(self, limit: int = ...) -> bytes: ...  # type: ignore
    def peek(self, n: int = ...) -> bytes: ...
    def read1(self, n: int | None) -> bytes: ...  # type: ignore

class _Writer(Protocol):
    def write(self, __s: str) -> Any: ...

class ZipFile:
    filename: Text | None
    debug: int
    comment: bytes
    filelist: list[ZipInfo]
    fp: IO[bytes] | None
    NameToInfo: dict[Text, ZipInfo]
    start_dir: int  # undocumented
    def __init__(self, file: StrPath | IO[bytes], mode: Text = ..., compression: int = ..., allowZip64: bool = ...) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def close(self) -> None: ...
    def getinfo(self, name: Text) -> ZipInfo: ...
    def infolist(self) -> list[ZipInfo]: ...
    def namelist(self) -> list[Text]: ...
    def open(self, name: _SZI, mode: Text = ..., pwd: bytes | None = ..., *, force_zip64: bool = ...) -> IO[bytes]: ...
    def extract(self, member: _SZI, path: StrPath | None = ..., pwd: bytes | None = ...) -> str: ...
    def extractall(self, path: StrPath | None = ..., members: Iterable[Text] | None = ..., pwd: bytes | None = ...) -> None: ...
    def printdir(self) -> None: ...
    def setpassword(self, pwd: bytes) -> None: ...
    def read(self, name: _SZI, pwd: bytes | None = ...) -> bytes: ...
    def testzip(self) -> str | None: ...
    def write(self, filename: StrPath, arcname: StrPath | None = ..., compress_type: int | None = ...) -> None: ...
    def writestr(self, zinfo_or_arcname: _SZI, bytes: bytes, compress_type: int | None = ...) -> None: ...

class PyZipFile(ZipFile):
    def writepy(self, pathname: Text, basename: Text = ...) -> None: ...

class ZipInfo:
    filename: Text
    date_time: _DT
    compress_type: int
    comment: bytes
    extra: bytes
    create_system: int
    create_version: int
    extract_version: int
    reserved: int
    flag_bits: int
    volume: int
    internal_attr: int
    external_attr: int
    header_offset: int
    CRC: int
    compress_size: int
    file_size: int
    def __init__(self, filename: Text | None = ..., date_time: _DT | None = ...) -> None: ...
    def FileHeader(self, zip64: bool | None = ...) -> bytes: ...

class _PathOpenProtocol(Protocol):
    def __call__(self, mode: str = ..., pwd: bytes | None = ..., *, force_zip64: bool = ...) -> IO[bytes]: ...

def is_zipfile(filename: StrPath | IO[bytes]) -> bool: ...

ZIP_STORED: int
ZIP_DEFLATED: int
ZIP64_LIMIT: int
ZIP_FILECOUNT_LIMIT: int
ZIP_MAX_COMMENT: int
