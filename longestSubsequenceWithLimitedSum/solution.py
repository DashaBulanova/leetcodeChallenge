class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        res = []
        for i in queries:
            r = self.define_max(nums, i)
            res.append(r)
        return res

    def define_max(self, nums: list[int], req: int) -> int:
        sum = 0
        e, s = 0, 0
        for e in range(len(nums)):
            sum += nums[e]
            if sum == req:
                return e-s
            while sum > req:
                sum -= nums[e]
                s += 1
        return e-s


"""
[4, 5, 2, 1]
s=3

i=3
res=2
sum=3

i=2
res=1
sum=2

i=1
res=1
sum=5
sum=0
res=0

i=0
res=1
sum=4
sum=0
res=0


"""
