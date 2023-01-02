class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = sum([x.isupper() for x in word])
        print(capitals)
        if capitals == len(word):
            return True
        if capitals == 0:
            return True
        if capitals == 1 and word[0].isupper():
            return True

        return False
