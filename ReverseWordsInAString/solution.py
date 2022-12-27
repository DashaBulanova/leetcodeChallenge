import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        q = collections.deque()
        result = []
        for i in range(len(s)+1):
            if i == len(s) or s[i] == " ":
                word = []
                while q:
                    word.append(q.popleft())
                if word:
                    result.append("".join(word))
            else:
                q.append(s[i])
        result.reverse()
        return " ".join(result)
