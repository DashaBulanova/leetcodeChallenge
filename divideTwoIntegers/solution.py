class Solution(object):

    def divide(self, dividend: int, divisor: int) -> int:

        positive = (dividend > 0) == (divisor > 0)

        dividend, divisor = abs(dividend),  abs(divisor)
        result = 0

        while dividend >= divisor:
            i = 0
            while divisor << (i+1) <= dividend:
                i += 1
            dividend -= (divisor << i)
            result += 1 << i

        return min(result if positive else -result, 2147483647)