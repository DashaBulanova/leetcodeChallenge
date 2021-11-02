from typing import List


# ["h", "e", "l", "l", "o"]
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        def swap(index_1: int, index_2: int):
            c = s[index_1]
            s[index_1] = s[index_2]
            s[index_2] = c

        while left < right:
            if s[left] != s[right]:
                swap(left, right)
            left += 1
            right -= 1
