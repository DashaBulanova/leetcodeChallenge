class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n=len(strs)
        i = 0
        result = []
        while True:
            if i>=len(strs[0]):
                return ''.join(result)
            c = strs[0][i] 
            for j in range(1,n):
                if i>=len(strs[j]) or strs[j][i] != c:
                    return ''.join(result)
            result.append(c)
            i+=1    
        return ""
