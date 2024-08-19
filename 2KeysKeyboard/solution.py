class Solution:
    def minSteps(self, n: int) -> int:
        operations = 0
        divider = 2
        while n > 1:
            while n % divider == 0:
                operations += divider
                n //= divider
            divider += 1
        return operations
