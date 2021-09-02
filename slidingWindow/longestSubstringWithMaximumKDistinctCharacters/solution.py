class Solution:
    def longest_substring_with_k_distinct(self, input, k):
        chars = dict()
        max_lengh = 0
        start_index = 0
        end_index = 0

        for c in input:
            end_index += 1
            chars[c] = chars.get(c, 0)+1
            while len(chars) > k:
                chars[input[start_index]] -= 1
                if chars[input[start_index]] == 0:
                    chars.pop(input[start_index])
                start_index += 1
            max_lengh = max(max_lengh, end_index-start_index)

        return len(input) if max_lengh == 0 else max_lengh
