"""
File to check the unitest
"""
import unittest  # It's a must, we needed to check
import cap_letter  # We import all the scripts that we want to check


class TestCap(unittest.TestCase):
    
    def test_one_word(self):

        text = 'python'
        result = cap_letter.cap_let(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):

        text = 'monty python'
        result = cap_letter.cap_let(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
        unittest.main()
