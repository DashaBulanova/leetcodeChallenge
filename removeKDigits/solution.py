from typing import List


class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:

        if len(nums) == k:
            return "0"

        nums = list(map(int, list(nums)))
        result = []
        min_index = -1
        filled_items = 0

        while filled_items != len(nums) - k:
            min_item = None

            for i in range(min_index + 1, k + filled_items + 1):
                if min_item is None or nums[i] < min_item:
                    min_item = nums[i]
                    min_index = i

            if not (min_item == 0 and len(result) == 0):
                result.append(min_item)
            filled_items += 1

        if len(result) == 0:
            return "0"
        return "".join(map(str, result))
