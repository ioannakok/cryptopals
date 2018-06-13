import binascii
import base64


def convert_hex_to_raw_bytes(str):
    return binascii.unhexlify(str)


def convert_hex_to_base64(hex_string):
    return base64.b64encode(convert_hex_to_raw_bytes(hex_string))


