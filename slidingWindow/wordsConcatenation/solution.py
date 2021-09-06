from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []

        words_map = dict()
        for word in words:
            words_map[word] = words_map.get(word, 0) + 1

        windows_size = len(words[0])
        windows_start = 0
        windows_end = windows_size
        matched = 0
        start_index = 0
        result = list()

        while windows_end <= len(s):
            substring = s[windows_start:windows_end]
            if substring in words_map:
                words_map[substring] -= 1
                matched += 1

                while words_map[substring] == -1:
                    words_map[s[start_index:start_index+windows_size]] += 1
                    matched -= 1
                    start_index += windows_size

                if matched == len(words):
                    result.append(start_index)

                windows_start += windows_size
                windows_end += windows_size
            else:
                while start_index < windows_start:
                    words_map[s[start_index:start_index+windows_size]] += 1
                    start_index += windows_size
                matched = 0
                windows_start += 1
                windows_end += 1
                start_index = windows_start

        return result
