class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        start = True

        def calc(x):
            return sum([int(i) ** 2 for i in str(x)])

        while start or fast != slow:
            start = False
            slow = calc(slow)
            fast = calc(calc(fast))
            if fast == 1:
                return True
        return False
