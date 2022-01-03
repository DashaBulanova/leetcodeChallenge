from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        he_trust = {i:0 for i in range(1, n+1)} # O(n)
        him_trust = {i:0 for i in range(1, n+1)} # O(n)
        for t in trust: #O(m)
            him_trust[t[1]]+=1
            he_trust[t[0]] +=1

        for i in range(1, n+1):
            if he_trust[i]==0 and him_trust[i]==n-1:
                return i
        return -1 #total complexity: 