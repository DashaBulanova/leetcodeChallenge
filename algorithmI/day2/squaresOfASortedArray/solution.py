from typing import List

"""
[-4, -1, 0, 3, 10]

16 1 0 9 100
 
O(n)+O(n log n) ~ O(n log n)

[-4, -1, 0, 3, 10]
left=0 right = 4
result_index = 4

100
16
result[4]=100
result_index=3
right=3

9
16
result[3]=16
result_index=2
left=1

1<3
9
1
result[2]=9
result_index=1
right=2

1<2
0
1
result[1]=1
result_index=0
right=1


"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        insert_index = len(nums) - 1

        while left <= right:
            right_sqr = nums[right] * nums[right]
            left_sqr = nums[left] * nums[left]
            result[insert_index] = max(right_sqr, left_sqr)

            if left_sqr > right_sqr:
                insert_index -= 1
                left += 1
            elif left_sqr < right_sqr:
                insert_index -= 1
                right -= 1
            else:
                if left != right:
                    result[insert_index - 1] = left_sqr
                    insert_index -= 2
                left += 1
                right -= 1

        return result
