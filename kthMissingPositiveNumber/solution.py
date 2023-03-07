class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] - (i + 1) >= k:
                return k + i
        return k + len(arr)
