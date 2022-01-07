class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        p1 = len(str1) - 1
        p2 = len(str2) - 1
        count1, count2 = 0, 0
        while p1 >= 0 and p2 >= 0:
            while p1 >= 0 and (str1[p1] == '#' or count1 > 0):
                count1 = count1 + 1 if str1[p1] == '#' else count1 - 1
                p1 -= 1
            while p2 >= 0 and (str2[p2] == '#' or count2 > 0):
                count2 = count2 + 1 if str2[p2] == '#' else count2 - 1
                p2 -= 1

            if p2 >= 0 and p1 >= 0 and str1[p1] != str2[p2]:
                return False
            p1 -= 1
            p2 -= 1

        while p1 >= 0 and (str1[p1] == '#' or count1 > 0):
            count1 = count1 + 1 if str1[p1] == '#' else count1 - 1
            p1 -= 1
        while p2 >= 0 and (str2[p2] == '#' or count2 > 0):
            count2 = count2 + 1 if str2[p2] == '#' else count2 - 1
            p2 -= 1

        return p1 == p2
