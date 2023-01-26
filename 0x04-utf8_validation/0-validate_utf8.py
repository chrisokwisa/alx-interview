#!/usr/bin/python3
""" contains a script - UTF-8 validation """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 """
    num_of_bytes = 0
    for byte in data:
        byte = byte & 0xFF

        if num_of_bytes == 0:
            if byte >> 5 == 0b110:
                num_of_bytes = 1
            elif byte >> 4 == 0b1110:
                num_of_bytes = 2
            elif byte >> 3 == 0b11110:
                num_of_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_of_bytes -= 1
    return num_of_bytes == 0
