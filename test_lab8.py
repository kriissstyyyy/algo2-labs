import unittest
from lab8 import solve_words


class TestWChain(unittest.TestCase):

    def test_example1(self):
        words = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate', 'tea', 'rat', 'a']
        self.assertEqual(solve_words(words), 6)

    def test_example2(self):
        words = ['b', 'bcad', 'bca', 'bad', 'bd']
        self.assertEqual(solve_words(words), 4)

    def test_example3(self):
        words = ['word', 'anotherword', 'yetanotherword']
        self.assertEqual(solve_words(words), 1)

    def test_single_word(self):
        self.assertEqual(solve_words(['hello']), 1)

    def test_single_letter_word(self):
        self.assertEqual(solve_words(['a']), 1)

    def test_two_words_connected(self):
        self.assertEqual(solve_words(['a', 'ab']), 2)

    def test_two_words_not_connected(self):
        self.assertEqual(solve_words(['abc', 'xyz']), 1)

    def test_linear_chain(self):
        self.assertEqual(solve_words(['a', 'ab', 'abc', 'abcd']), 4)

    def test_branching_chain(self):
        words = ['c', 'a', 'ca', 'at', 'cat', 'bat']
        self.assertEqual(solve_words(words), 3)

    def test_all_single_letters(self):
        self.assertEqual(solve_words(['a', 'b', 'c', 'd']), 1)

    def test_empty_list(self):
        self.assertEqual(solve_words([]), 0)

    def test_long_chain(self):
        self.assertEqual(solve_words(['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']), 6)


if __name__ == '__main__':
    unittest.main()