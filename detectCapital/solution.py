class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all([x.isupper() for x in word]):
            return True
        if all([x.islower() for x in word]):
            return True
        if word[0].isupper() and all([word[x].islower() for x in range(1, len(word))]):
            return True

        return False
