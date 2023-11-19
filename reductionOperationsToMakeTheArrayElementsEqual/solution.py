import heapq


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                count += i + 1

        return count


"""
[1,1,2,2,3]
3,2,2,1,1
i = 0
count=1
i=1
i=2
count=4
i=3

5,4,3,1,1
5=>4
4,4,3,1,1
4=>3
3,4,3,1,1
4=>3
3,3,3,1,1
3=>1
3=>1
3=>1

3=>2
2=>1
2=>1
2=>1
"""
