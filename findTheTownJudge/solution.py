from typing import List


class Solution(object):

    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if N == 1 and len(trust) == 0:
            return 1
        if N == 2 and len(trust) == 1:
            return trust[0][1]
        judges_candidates = set()
        people = set()

        for connection in trust:
            a = connection[0]
            b = connection[1]

            judges_candidates.add(b)
            people.add(a)

        diff = judges_candidates.difference(people)

        if len(diff) == 1 and len(people) == N-1:
            if len(trust) == N-1 and len(judges_candidates) >= N-1:
                return -1
            else:
                return diff.pop()
        else:
            return -1
