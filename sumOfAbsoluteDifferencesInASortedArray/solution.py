class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        l = len(nums)
        result = [0] * l
        sr = total
        sl = 0

        for i in range(len(nums)):
            sr -= nums[i]
            result[i] = sum([sr - nums[i] * (l - 1 - i), nums[i] * i - sl])
            sl += nums[i]
            print(result)
        return result


"""
[1, 4, 6, 8, 10]
total=29,l=5
sr=29
sl=0

i=0
sr=28
result[0]=(28-1*4)=24
sl=1
i=1
sr=24
result[1]=24-4*3=12+4*1-1=12+4-1=15
sl=5
i=2
sr=18
result[2]=18-6*2=6+6*2-5=6+12-5=13

"""
