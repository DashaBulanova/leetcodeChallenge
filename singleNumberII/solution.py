from typing import List


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = set()
        sum = 0
        for i in nums:
            ones.add(i)
            sum += i

        result = 0
        for i in ones:
            result += 3*i

        return int((result - sum)/2)
