from challenge1 import convert_hex_to_raw_bytes

string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
char_frequency = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0,
                  'j': 0.2, 'k': 0.7, 'l': 4.0, 'm': 2.4, 'n': 6.8, 'o': 7.5, 'p': 1.1, 'q': 0.1, 'r': 6.0,
                  's': 6.3, 't': 9.0, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1, ' ': 13.0}


def find_key(word):
    decoded_word = convert_hex_to_raw_bytes(word)
    data = {}
    for key in range(256):
        message = xor_word_against_char(decoded_word, key)
        score = get_word_score(message)
        data[score] = (key, message)

    maximum_score = max(list(data.keys()))

    print("Key: " + chr(data[maximum_score][0]))
    print("Message: " + str(data[maximum_score][1]))


def xor_word_against_char(word, key):
    output = b''
    for char in word:
        output += bytes([char ^ key])
    return output


def get_word_score(word):
    score = 0
    for char in word.lower():
        score += get_char_score(char)
    return score


def get_char_score(char):
    return char_frequency.get(chr(char), 0)


find_key(string)
