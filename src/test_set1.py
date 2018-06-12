import unittest
import challenge1


class TestSetOne(unittest.TestCase):

    def test_hex_should_be_converted_to_base64(self):
        string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(challenge1.convert_hex_to_base64(string), expected)


if __name__ == '__main__':
    unittest.main()
