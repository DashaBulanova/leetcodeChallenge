import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0

        result = 0
        while m > 0 and n > 0:
            msb_m = self.get_most_significant_bit(m)
            msb_n = self.get_most_significant_bit(n)

            if msb_m != msb_n:
                return result

            result += pow(2, msb_m)

            m -= 2 ** msb_m
            n -= 2 ** msb_n

        return result

    def get_most_significant_bit(self, m):
        return int(math.log2(m))
