import struct

def pack_into(fmt: str|bytes, buffer: bytearray, offset: int, *v) -> None:
    """
    Pack the values v1, v2, ... according to the format string and write\n
    the packed bytes into the writable buffer buf starting at offset. Note\n
    that the offset is a required argument. See help(struct) for more\n
    on format strings.\n
    """

    struct.pack_into(fmt, buffer, offset, *v)