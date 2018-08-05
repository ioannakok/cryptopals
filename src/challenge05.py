stanza = "Burning 'em, if you ain't quick and nimble " \
         "I go crazy when I hear a cymbal"
key = "ICE"


def repeating_key_xor(word, key):
    word = word.encode()
    counter = 0
    output = b''

    for char in word:
        output += bytes([char ^ ord(key[counter])])

        counter = 0 if counter == len(key) - 1 else counter + 1

    return output.hex()


print(repeating_key_xor(stanza, key))
