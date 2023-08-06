#!/usr/bin/env python
import typing
import io
import struct
import os

__all__ = ["TemporarySeek", "Reader", "Writer"];

class InvalidEndiannessError(Exception):
    pass

class Stream:
    def __init__(self, stream: io.BytesIO, endian: str = "little"):
        """
        A stream for reading and writing data
        """
        self._stream = stream;
        if endian == "little" or endian == '<':
            self._endian = '<';

        elif endian == "big" or endian == '>':
            self._endian = '>';

        else:
            raise InvalidEndiannessError("Not a valid endianness");
        
    def seek(self, offset: int) -> None:
        self._stream.seek(offset);

    def skip(self, n: int) -> None:
        self._stream.seek(n, os.SEEK_CUR);

    def getbuffer(self) -> memoryview:
        return self._stream.getbuffer()

    def getvalue(self) -> bytes:
        return self._stream.getvalue()

    def tell(self) -> int:
        return self._stream.tell();

class TemporarySeek:
    def __init__(self, stream: Stream, offset: int):
        self._stream: Stream = stream;
        self._temp_offset: int = offset;
        self._original_offset: int = self._stream.tell();

    def __enter__(self):
        self._stream.seek(self._temp_offset);
        return self._temp_offset;

    def __exit__(self, *args):
        self._stream.seek(self._original_offset);

class Reader(Stream):
    """
    A stream to read data from
    """

    def __init__(self, data: bytes, endian: str):
        stream = io.BytesIO(memoryview(data));
        super().__init__(stream, endian);

    @classmethod
    def from_writer(cls, writer: Stream):
        return cls(writer.getvalue(), writer._endian);

    # Read "n" number of bytes
    def read(self, n: int) -> bytes:
        return self._stream.read(n);

    # Read a specific amount of bytes based on the format
    def readf(self, fmt: str) -> typing.Union[int, float, bool, bytes, tuple]:
        size: int = struct.calcsize(fmt);
        value: tuple = struct.unpack(self._endian + fmt, self._stream.read(size));
        
        if len(value) == 1:
            return value[0];

        else:
            return value;

    # Read a string of "str_len" length, or null terminated if not provided
    def read_string(self, str_len: int = 0, encoding: str = "utf-8") -> str:
        if str_len != 0:
            return self._stream.read(str_len).decode(encoding);

        else:
            # https://ourpython.com/python/clean-way-to-read-a-null-terminated-c-style-string-from-a-file
            buf: typing.List[bytes] = list()
            while True:
                b = self._stream.read(1);
                if b is None or b == b'\0':
                    return b''.join(buf).decode(encoding);
                else:
                    buf.append(b);


class Writer(Stream):
    """
    A stream to write data into
    """

    def __init__(self, data: bytes, endian: str):
        stream = io.BytesIO(memoryview(data));
        super().__init__(stream, endian);

    @classmethod
    def from_reader(cls, reader: Reader):
        return cls(reader.getvalue(), reader._endian);

    def write(self, data: bytes) -> None:
        self._stream.write(data);
        
    def writef(self, fmt: str, data: typing.Union[int, float, bytes, bool]) -> None:
        self._stream.write(struct.pack(self._endian + fmt, data));
