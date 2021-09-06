class Solution:
    def find_permutation(self, str, pattern):
        map = dict()
        for p in pattern:
            if p in map:
                map[p] += 1
            else:
                map[p] = 1

        window_start = 0
        matched = 0

        for window_end in range(len(str)):
            right_char = str[window_end]
            if right_char in map:
                map[right_char] -= 1
                if map[right_char] == 0:
                    matched += 1

            if matched == len(map):
                return True

            if window_end-window_start+1 >= len(pattern):
                left_char = str[window_start]
                if left_char in map:
                    if map[left_char] == 0:
                        matched -= 1
                    map[str[window_start]] += 1
                window_start += 1

        return False
