import sys


class Solution(object):

    def __init__(self):
        self.recursion_limit = sys.getrecursionlimit()
        self.recursion_count = 0

    def isHappy(self, n: int) -> bool:

        self.recursion_count += 1
        if self.recursion_count >= 958:
            return False

        sum = 0
        for d in str(n):
            d1 = int(d)
            sum += d1 * d1


        if sum == 1:
            return True
        else:
            return self.isHappy(sum)
