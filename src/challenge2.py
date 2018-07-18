str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"


def convert_hex_string_to_int(string):
    return int(string, base=16)


def xor_strings(str1, str2):
    if len(str1) == len(str2):
        return hex(convert_hex_string_to_int(str1) ^ convert_hex_string_to_int(str2))
    else:
        return


print(xor_strings(str1, str2))