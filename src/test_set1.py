import unittest
import challenge1
import challenge2


class TestSetOne(unittest.TestCase):

    def setUp(self):
        self.string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    def test_hex_should_be_converted_to_raw_bytes(self):
        expected = b"I'm killing your brain like a poisonous mushroom"
        self.assertEqual(challenge1.convert_hex_to_raw_bytes(self.string), expected)

    def test_hex_should_be_converted_to_base64(self):
        expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(challenge1.convert_hex_to_base64(self.string), expected)

    def test_should_produce_integer_from_hex_string(self):
        self.assertEqual(challenge2.convert_hex_string_to_int("16"), 22)
        self.assertEqual(challenge2.convert_hex_string_to_int("a"), 10)
        self.assertEqual(challenge2.convert_hex_string_to_int("f"), 15)
        self.assertEqual(challenge2.convert_hex_string_to_int("5b"), 91)

    def test_should_produce_xor_combination_of_strings(self):
        string1 = "1c0111001f010100061a024b53535009181c"
        string2 = "686974207468652062756c6c277320657965"
        expected = "0x746865206b696420646f6e277420706c6179"
        self.assertEqual(challenge2.xor_strings(string1, string2), expected)


if __name__ == '__main__':
    unittest.main()
