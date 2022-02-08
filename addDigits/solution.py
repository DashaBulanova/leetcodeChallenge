
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        reminder = num % 9 
        if reminder == 0:
            return 9
        return reminder
