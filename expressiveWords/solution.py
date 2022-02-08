from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        if not words:
            return 0

        def compress(s: str):
            groups = []
            curr = None
            count = 0
            for c in s:
                if curr is None:
                    curr = c
                    count += 1
                elif c == curr[0]:
                    count += 1
                else:
                    groups.append((curr, count))
                    curr = c
                    count = 1

            groups.append((curr, count))
            return groups

        def is_stretchy(query, reference) -> bool:
            if len(query) != len(reference):
                return False

            p1 = 0
            p2 = 0

            while p2 < len(query):
                if reference[p1][0] != query[p2][0]:
                    return False
                else:
                    if reference[p1][1] < query[p2][1]:
                        return False
                    elif reference[p1][1] == query[p2][1]:
                        p1 += 1
                        p2 += 1
                    elif reference[p1][1] < 3:
                        return False
                    else:
                        p1 += 1
                        p2 += 1
            return True

        stretchy = compress(s)

        result = 0
        for word in words:
            w = compress(word)
            if is_stretchy(w, stretchy):
                result += 1

        return result
