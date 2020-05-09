class Solution(object):
    # time complexity O(sqrt(num))
    def isPerfectSquare(self, num: int) -> bool:

        for i in range(1, num):
            pow = i ** 2
            if pow == num:
                return True
            elif pow > num:
                return False

        return False

    # time complexity O(log(sqrt(N)))
    def binarySearch(self, num: int) -> bool:
        low = 1
        high = num

        while low <= high:
            mid = low + (high - low) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1

        return False