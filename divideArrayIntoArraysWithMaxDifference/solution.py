class Solution:
    def divideArray(self, nums: list[int], l: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        k = n // 3
        result = [[0]*3]*k
        for i in range(0, k):
            result[i] = nums[i*3:i*3+3]
            if result[i][2]-result[i][0] > l:
                return []
        return result 

'''
[33,26,4,18,16,24,24,15,8,18,34,20,24,16,3]
 3,4,8 15,16,16, 18,18,20 24,24,24 26,33,34

i=0
result[0]=nums[0:3]=[3,4,8]
result[1]=nums[1*3=3:6]=[15,16,16]
result[2]=nums[6:9]=
'''
