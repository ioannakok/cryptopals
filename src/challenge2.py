

def convert_hex_string_to_int(string):
    return int(string, base=16)


def xor_strings(str1, str2):
    return hex(convert_hex_string_to_int(str1) ^ convert_hex_string_to_int(str2))

