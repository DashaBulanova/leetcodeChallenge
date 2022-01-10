from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            raise ValueError('length of s should be more than 1')

        stack = deque()
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in mapping:
                if len(stack) == 0:
                    return False
                open_br = stack.pop()
                if mapping[c] != open_br:
                    return False
            else:
                stack.append(c)

        return True if len(stack) == 0 else False
