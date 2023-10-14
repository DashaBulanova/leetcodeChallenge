class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(x):
            return sum([int(i) ** 2 for i in str(x)])

        slow = n
        fast = n
        while True:
            slow = calc(slow)
            fast = calc(calc(fast))
            if fast == 1:
                return True
            if fast == 89:
                return False
            if fast == slow:
                return False
