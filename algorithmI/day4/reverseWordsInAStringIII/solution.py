class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []

        def swap(word, index_1, index_2):
            c = word[index_1]
            word[index_1] = word[index_2]
            word[index_2] = c

        def reverse_word(word: str) -> str:
            left = 0
            right = len(word) - 1
            r = list(word)
            while left < right:
                if r[left] != r[right]:
                    swap(r, left, right)
                left += 1
                right -= 1
            return ''.join(r)

        for i in range(len(words)):
            res.append(reverse_word(words[i]))

        return ' '.join(res)
