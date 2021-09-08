from typing import List


class Solution:
    def remove_duplicates(self, arr: List[int]):
        result = 1
        last_unique_index = 0
        check_index = 1

        while check_index < len(arr):
            check_item = arr[check_index]
            last_unique_item = arr[last_unique_index]

            if last_unique_item != check_item:
                if check_index != last_unique_index+1:
                    arr[last_unique_index+1] = check_item
                    arr[check_index] = -1
                last_unique_index += 1
                result += 1
            check_index += 1

        return result

