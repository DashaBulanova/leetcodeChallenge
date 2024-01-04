class Solution:
    def minOperations(self, nums: list[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        result = 0
        for k,v in d.items():
            if v>6 and v % 6 == 1:
                v -= 3
                result += 1
            if v%6==0 or v%6>1:
                result += (v // 6) * 2
                v = v%6
            if v%3 == 0 or v%3 == 2:
                result += v//3
                v = v%3
            if v%2 == 0:
                result += v//2
            else:
                return -1
        return result
