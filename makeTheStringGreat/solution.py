from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        d = deque()
        for c in s:
            if not d:
                d.append(c)
            else:
                item = d[-1]
                if c.lower() == item.lower() and c != item:
                    d.pop()
                else:
                    d.append(c)
        return "".join(d)
