class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(x):
            return sum([int(i) ** 2 for i in str(x)])

        slow = n
        while slow != 1:
            slow = calc(slow)
            if slow == 89:
                return False
        return True
