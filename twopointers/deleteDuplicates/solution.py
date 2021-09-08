from typing import List


class Solution:
    def remove_duplicates(self, arr: List[int]):
        last_unique_index = 0
        check_index = 1

        while check_index < len(arr):
            if arr[last_unique_index] != arr[check_index]:
                if check_index != last_unique_index + 1:
                    arr[last_unique_index + 1] = arr[check_index]
                    arr[check_index] = -1
                last_unique_index += 1
            check_index += 1

        return last_unique_index + 1
