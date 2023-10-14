class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        while slow != 1:
            slow = sum([int(i) ** 2 for i in str(slow)])
            if slow == 89:
                return False
        return True
