

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        need_to_close = list()

        window_start = 0
        res = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char == '(':
                need_to_close.append(window_end)
            else:
                if len(need_to_close) != 0:
                    need_to_close.pop()
                    window_size = window_end - need_to_close[-1] if need_to_close else window_end - window_start + 1
                    res = max(window_size, res)
                else:
                    window_start = window_end + 1

        return res
