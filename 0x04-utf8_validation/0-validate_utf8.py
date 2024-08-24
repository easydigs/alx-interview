#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    def is_start_byte(byte):
        """Determine if a byte is a valid start of a multi-byte character."""
        if byte >> 7 == 0b0:  # 1-byte character (0xxxxxxx)
            return 0
        elif byte >> 5 == 0b110:  # 2-byte character (110xxxxx)
            return 1
        elif byte >> 4 == 0b1110:  # 3-byte character (1110xxxx)
            return 2
        elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
            return 3
        return -1  # Invalid start byte

    def is_continuation_byte(byte):
        """Check if the byte is a valid continuation byte (10xxxxxx)."""
        return byte >> 6 == 0b10

    i = 0
    n = len(data)

    while i < n:
        start_byte = data[i]
        num_bytes = is_start_byte(start_byte)

        if num_bytes == -1:
            return False

        for j in range(1, num_bytes + 1):
            if i + j >= n or not is_continuation_byte(data[i + j]):
                return False

        i += num_bytes + 1

    return True
