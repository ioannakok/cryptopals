import binascii
import base64

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def convert_hex_to_raw_bytes(str):
    return binascii.unhexlify(str)


def convert_hex_to_base64(hex_string):
    return base64.b64encode(convert_hex_to_raw_bytes(hex_string))


print(convert_hex_to_base64(string))
