class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        i2 = i3 = i5 = 0
        while len(ugly_numbers) < n:
            v2 = ugly_numbers[i2]*2
            v3 = ugly_numbers[i3]*3
            v5 = ugly_numbers[i5]*5
            min_v = min(v2, v3, v5)
            ugly_numbers.append(min_v)
            if min_v == v2:
                i2 += 1
            if min_v == v3:
                i3 += 1
            if min_v == v5:
                i5 += 1

        return ugly_numbers[n-1]
