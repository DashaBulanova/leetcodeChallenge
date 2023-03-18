class TrieNode:
    def __init__(self):
        self.__children: list[TrieNode | None] = [None for _ in range(26)]
        self.__end_of_word = False

    @staticmethod
    def __get_children_number(word: str, i: int):
        return ord(word[i]) - 97

    def seach(self, word: str, i: int) -> bool:
        j = self.__get_children_number(word, i)

        if not self.__children[j]:
            return False

        if i == len(word) - 1:
            return self.__end_of_word

        return self.__children[j].seach(word, i + 1)

    def insert(self, word: str, i: int) -> None:
        j = self.__get_children_number(word, i)

        if not self.__children[j]:
            self.__children[j] = TrieNode()

        if i == len(word) - 1:
            self.__end_of_word = True
            return

        return self.__children[j].insert(word, i + 1)

    def startsWith(self, prefix: str, i: int) -> bool:
        j = self.__get_children_number(prefix, i)

        if not self.__children[j]:
            return False

        if i == len(prefix) - 1:
            return True

        return self.__children[j].startsWith(prefix, i + 1)


class Trie:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        self.__root.insert(word, 0)

    def search(self, word: str) -> bool:
        return self.__root.seach(word, 0)

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix) or any(child.startswith(prefix) for child in self.root.children.values())
