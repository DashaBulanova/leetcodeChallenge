class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = dict()
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        window_start = 0
        matched = 0
        res = []

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in t_map:
                t_map[right_char] -= 1
                if t_map[right_char] == 0:
                    matched += 1

            if matched == len(t_map):
                while s[window_start] not in t_map or t_map[s[window_start]] < 0:
                    if s[window_start] in t_map:
                        t_map[s[window_start]] += 1
                    window_start += 1

                res.append(s[window_start:window_end + 1])
                t_map[s[window_start]] += 1
                matched -= 1
                window_start += 1

        return "" if len(res) == 0 else min(res, key=len)
