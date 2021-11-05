class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        needs = {}
        for i in s1:
            needs[i] = needs[i]+1 if i in needs else 1

        start = 0
        total_needs = len(s1)

#Space complexity: in worst case 26 in best case len(s1): O(1)
#Time complexity: O(len(s1))+O(2*len(s2))=O(l1+l2-l1)

        for end in range(len(s2)):
            if s2[end] in needs:
                if needs[s2[end]] == 0:
                    while s2[start] != s2[end]:
                        needs[s2[start]] += 1
                        total_needs += 1
                        start += 1
                    needs[s2[start]] += 1
                    total_needs += 1
                    start += 1
                needs[s2[end]] -= 1
                total_needs -= 1
                if total_needs == 0:
                    return True
            else:
                while start <= end:
                    if s2[start] in needs:
                        needs[s2[start]] += 1
                        total_needs += 1
                    start += 1
        return False
