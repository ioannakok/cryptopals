import binascii
import base64


def convert_hex_to_base64(hex_string):
    byte_str = binascii.unhexlify(hex_string)
    return base64.b64encode(byte_str)

