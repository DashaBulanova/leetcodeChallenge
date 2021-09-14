from typing import List


class Solution:
    def search_triplets(self, arr):
        triplets = []
        sorted_arr = sorted(arr)  # O(N*log(N))
        pointer_1 = 0

        while sorted_arr[pointer_1] <= 0:  # O(N)
            target = sorted_arr[pointer_1]
            res = self.find_pair(abs(target), pointer_1 + 1, nums=sorted_arr)
            if res:
                triplets.extend(res)

            pointer_1 += 1
        return triplets

    def find_pair(self, target: int, left_index: int, nums: List[int]) -> List[list[int]]:
        right_index = len(nums) - 1
        result = []
        while left_index < right_index:
            right = nums[right_index]
            left = nums[left_index]

            if left + right > target:
                right_index -= 1
            elif left + right < target:
                left_index += 1
            else:
                result.append([-target, right, left])
                left_index += 1
                right_index -= 1

        return result
