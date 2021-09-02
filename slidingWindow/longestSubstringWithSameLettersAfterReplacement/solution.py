class Solution:
    def length_of_longest_substring1(self, str1, k):
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

        # Try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in frequency_map:
                frequency_map[right_char] = 0
            frequency_map[right_char] += 1
            max_repeat_letter_count = max(
                max_repeat_letter_count, frequency_map[right_char])

            # Current window size is from window_start to window_end, overall we have a letter which is
            # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = str1[window_start]
                frequency_map[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length


    def length_of_longest_substring(self, str, k):
        chars_map = dict()
        longest_substring = 0
        most_frequently_char = 0
        start_window = 0

        for end_window in range(len(str)):
            c = str[end_window]
            chars_map[c] = chars_map.get(c, 0) + 1
            most_frequently_char = max(most_frequently_char, chars_map[c])

            while end_window - start_window + 1 - most_frequently_char > k:
                chars_map[str[start_window]] -= 1
                if chars_map[str[start_window]] == 0:
                    chars_map.pop(str[start_window])
                start_window += 1

            longest_substring = max(longest_substring, end_window - start_window + 1)
        return longest_substring
