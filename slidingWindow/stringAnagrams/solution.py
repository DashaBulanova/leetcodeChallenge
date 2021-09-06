class Solution:
    def find_string_anagrams(self, str, pattern):
        pattern_map = dict()
        for ch in pattern:
            pattern_map[ch] = pattern_map.get(ch, 0) + 1

        window_start = 0
        matched = 0
        result = []

        for window_end in range(len(str)):
            if str[window_end] in pattern_map:
                pattern_map[str[window_end]] -= 1
                if pattern_map[str[window_end]] == 0:
                    matched += 1

            if matched == len(pattern_map):
                result.append(window_start)

            if window_end - window_start + 1 >= len(pattern):
                if str[window_start] in pattern_map:
                    if pattern_map[str[window_start]] == 0:
                        matched -= 1
                    pattern_map[str[window_start]] += 1
                window_start += 1

        return result
