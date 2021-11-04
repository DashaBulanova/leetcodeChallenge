"""
"abcabcbb"
s=0
e=0
c=a
chars={'c':1}
result = 1

e=1
c=b
chars={'a':1, b:1}
result = 2

e=2
c=c
chars={'c':1, b:1, c:1}
result = 3

e=3
c=1
chars={'a':0, b:1, c:1}
s=1
result = 3
"""





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start_pointer = 0
        result = 0

        def exists(c):
            return c in chars and chars[c] == 1

        for end_pointer in range(len(s)):
            c = s[end_pointer]
            while exists(c):
                chars[s[start_pointer]] = 0
                start_pointer += 1

            chars[s[end_pointer]] = 1
            result = max(result, end_pointer-start_pointer+1)

        return result
