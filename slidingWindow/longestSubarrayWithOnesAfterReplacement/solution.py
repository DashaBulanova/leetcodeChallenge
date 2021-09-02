class Solution:
    def length_of_longest_substring(self, arr, k):
        need_to_change = 0
        window_start = 0
        longest_substring = 0

        for window_end in range(len(arr)):
            i = arr[window_end]
            if i == 0:
                need_to_change += 1

            if need_to_change > k:
                if arr[window_start] == 0:
                    need_to_change -= 1
                window_start += 1

            longest_substring = max(longest_substring, window_end - window_start + 1)
        return longest_substring
