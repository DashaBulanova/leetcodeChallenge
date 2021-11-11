class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()

        acc = 0
        curr = n
        while acc not in sums:
            if acc != 0:
                sums.add(acc)
                curr = acc
            acc = 0
            for i in list(str(curr)):
                acc += int(i) * int(i)
            if acc == 1:
                return True
        return False
