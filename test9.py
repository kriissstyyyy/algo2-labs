import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lab9 import Trie, TrieNode, build_trie


class TestTrieNode(unittest.TestCase):
    def test_initial_children_empty(self):
        node = TrieNode()
        self.assertEqual(node.children, {})

    def test_initial_is_end_of_word_false(self):
        node = TrieNode()
        self.assertFalse(node.is_end_of_word)


class TestTrieInsert(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_single_word(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))

    def test_insert_multiple_words(self):
        words = ["apple", "app", "application", "apply"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.search(word))

    def test_insert_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_insert_duplicate_word(self):
        self.trie.insert("hello")
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))


class TestTrieSearch(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for word in ["apple", "app", "banana"]:
            self.trie.insert(word)

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("apple"))

    def test_search_missing_word(self):
        self.assertFalse(self.trie.search("orange"))

    def test_search_prefix_only(self):
        self.assertFalse(self.trie.search("ap"))

    def test_search_empty_trie(self):
        empty_trie = Trie()
        self.assertFalse(empty_trie.search("word"))

    def test_search_case_sensitive(self):
        self.assertFalse(self.trie.search("Apple"))
        self.assertFalse(self.trie.search("APPLE"))


class TestTrieStartsWith(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for word in ["apple", "app", "banana"]:
            self.trie.insert(word)

    def test_starts_with_valid_prefix(self):
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))

    def test_starts_with_full_word(self):
        self.assertTrue(self.trie.starts_with("apple"))

    def test_starts_with_invalid_prefix(self):
        self.assertFalse(self.trie.starts_with("xyz"))

    def test_starts_with_empty_prefix(self):
        self.assertTrue(self.trie.starts_with(""))

    def test_starts_with_prefix_longer_than_word(self):
        self.assertFalse(self.trie.starts_with("apple123"))


class TestBuildTrie(unittest.TestCase):
    def test_returns_trie_instance(self):
        result = build_trie(["hello", "world"])
        self.assertIsInstance(result, Trie)

    def test_all_patterns_inserted(self):
        patterns = ["cat", "car", "card", "care", "careful"]
        trie = build_trie(patterns)
        for pattern in patterns:
            self.assertTrue(trie.search(pattern))

    def test_empty_list(self):
        trie = build_trie([])
        self.assertFalse(trie.search("anything"))

    def test_prefixes_work_after_build(self):
        trie = build_trie(["python", "pytest", "pycharm"])
        self.assertTrue(trie.starts_with("py"))
        self.assertTrue(trie.starts_with("pyt"))
        self.assertFalse(trie.starts_with("java"))

    def test_non_inserted_word_not_found(self):
        trie = build_trie(["apple", "banana"])
        self.assertFalse(trie.search("cherry"))

    def test_single_character_words(self):
        trie = build_trie(["a", "b", "c"])
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.search("b"))
        self.assertFalse(trie.search("d"))


if __name__ == "__main__":
    unittest.main()

