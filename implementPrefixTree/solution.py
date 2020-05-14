import string
from typing import List


class TrieNode:
    def __init__(self):
        self.alphabet = [None] * 27
        self.children = None

    def insert(self, word: List) -> None:
        if word[0] == '$':
            self.alphabet[26] = '$'
        else:
            index = string.ascii_letters.index(word[0])
            word.pop(0)
            if self.alphabet[index] is None:
                self.alphabet[index] = TrieNode()
            self.alphabet[index].insert(word)

    def search(self, word: List) -> bool:
        if word[0] == '$':
            if self.alphabet[26] is not None:
                return True
            else:
                return False

        index = string.ascii_letters.index(word[0])
        if self.alphabet[index] is None:
            return False
        else:
            word.pop(0)
            return self.alphabet[index].search(word)

    def startsWith(self, word: List) -> bool:
        if len(word) == 0:
            return True

        index = string.ascii_letters.index(word[0])
        if self.alphabet[index] is None:
            return False
        else:
            word.pop(0)
            return self.alphabet[index].startsWith(word)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root.insert(list(str(word+'$')))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.root.search(list(str(word+'$')))


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.startsWith(list(str(prefix)))
