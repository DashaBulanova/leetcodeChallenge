class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for c in sentence:
            if c not in alphabet:
                alphabet.add(c)
        return len(alphabet) == 26
