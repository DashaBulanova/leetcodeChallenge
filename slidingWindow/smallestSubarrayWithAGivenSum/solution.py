class Solution:
    def smallest_subarray_with_given_sum(self, s, arr):
        result = 0
        acc = 0
        window_lenght = 0
        start = 0
        for i in range(0, len(arr)):
            acc += arr[i]
            window_lenght += 1
            while acc >= s:
                result = window_lenght if result == 0 else min(result, window_lenght)
                acc -= arr[start]
                start += 1
                window_lenght -= 1

        return result
