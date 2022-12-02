
import string


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dict1 = [0] * 26
        dict2 = [0] * 26

        for i in range(len(word1)):
            dict1[ord(word1[i])-97] += 1
            dict2[ord(word2[i])-97] += 1

        l1 = list()
        l2 = list()
        for i in range(26):
            if dict1[i] == dict2[i]:
                continue
            if dict1[i] == 0 and dict2[i] != 0:
                return False
            if dict1[i] != 0 and dict2[i] == 0:
                return False

            l1.append(dict1[i])
            l2.append(dict2[i])
        
        l1.sort()
        l2.sort()

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
         
        return True