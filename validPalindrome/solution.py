class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = ''
        for c in s.lower():
            if ord(c) in range(97, 123) or ord(c) in range(48, 58):
                cleared += c

        return cleared == cleared[::-1]