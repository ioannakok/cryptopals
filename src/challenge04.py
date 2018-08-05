from challenge03 import find_key


def find_encrypted_message():
    counter = 1
    with open('../data/challenge4-data.txt') as file:
        for line in file:
            message = {"No": counter, "encrypted": line, "decrypted": find_key(line.rstrip())}
            counter += 1
            print(message)


find_encrypted_message()

