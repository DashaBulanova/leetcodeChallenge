class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        import re
        pattern = word.replace(".", "[a-z]")
        pattern = "^"+pattern+"$"

        for word in self.words:
            match = re.search(pattern, word)
            if match:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
