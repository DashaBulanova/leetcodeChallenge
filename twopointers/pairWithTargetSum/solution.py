class Solution:
    def pair_with_targetsum(self, arr, target_sum):
        pointer_1 = 0
        pointer_2 = len(arr)-1

        while pointer_1 != pointer_2:
            sum = arr[pointer_1] + arr[pointer_2]
            if sum == target_sum:
                return [pointer_1, pointer_2]
            elif sum > target_sum:
                pointer_2 -= 1
            else:
                pointer_1 += 1

        return [-1, -1]

