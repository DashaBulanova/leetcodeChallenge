class Solution(object):
    # time complexity O(sqrt(num))
    def isPerfectSquare(self, num: int) -> bool:

        for i in range(1, 46341):
            pow = i ** 2
            if pow == num:
                return True
            elif pow > num:
                return False

        return False

    # time complexity O(log(sqrt(N)))
    def binarySearch(self, num: int) -> bool:
        low = 1
        high = 46340
        mid = 0

        while low != mid != high:
            mid = int((high - low) // 2) + low
            pow = mid ** 2

            if pow == num:
                return True

            high = mid - 1 if pow > num else high
            low = mid + 1 if pow < num else low

        return mid ** 2 == num