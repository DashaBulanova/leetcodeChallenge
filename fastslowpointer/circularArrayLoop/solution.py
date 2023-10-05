from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def assert_direction(original_direction, current):
            if original_direction == 'forward':
                assert nums[current] >= 0
            if original_direction == 'backward':
                assert nums[current] < 0

        def next(original_direction, index):
            new_index = (index + nums[index]) % len(nums)
            assert_direction(original_direction, new_index)
            assert new_index != index
            return new_index

        for i in range(len(nums)):
            fast = slow = i

            direction = 'forward' if nums[i] >= 0 else 'backward'
            first_run = True

            try:
                while first_run or slow != fast:
                    first_run = False
                    slow = next(direction, slow)
                    fast = next(direction, fast)
                    fast = next(direction, fast)

                return True
            except AssertionError:
                continue

        return False
