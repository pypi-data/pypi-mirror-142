# Extended IO
Extended IO is module designed to extend the i/o handling of binary files in python.

## Documentation
Please check the [wiki](https://gitlab.com/Nitr4m12/extendedio/-/wikis/home) for documentation.

## Example Usage
```
>>> from extendedio import Reader
>>> reader = Reader(b"\x48\x49\x21")
>>> reader.read_string(3)
"HI!"

>>> from extendedio import Writer
>>> writer = Writer(bytes(), "little")
>>> writer.writef("3s", b"\x48\x49\x21")
>>> writer.getvalue()
b'HI!'

```
