class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(x):
            return sum([int(i) ** 2 for i in str(x)])

        slow = n
        fast = n
        while True:
            for i in range(2):
                if i == 0:
                    slow = calc(slow)
                fast = calc(fast)
                if fast == 1:
                    return True
                if fast == 89:
                    return False
            if fast == slow:
                return False
