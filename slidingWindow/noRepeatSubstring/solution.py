class Solution:
    def non_repeat_substring(self, str):
        unique = dict()
        result = 0
        window_start = 0
        for window_end in range(len(str)):
            c = str[window_end]
            if c in unique:
                until_index = unique.get(c) + 1
                while window_start < until_index:
                    unique.pop(str[window_start])
                    window_start += 1
            unique[c] = window_end
            result = max(result, window_end - window_start + 1)
        return result
