class Solution:
    def pivotInteger(self, n: int) -> int:
        j = n
        left = sum([i for i in range(n+1)])
        right = 0

        while left > right:
            right += j

            if left == right:
                return j
            else:
                left -= j
                j -= 1  

        return -1

"""
1 2 3 4 5 6 7 8
total = 36
j=8
right = 8
left=36-8=28
j=7
right=15
lelf=21
j=6

right=21

36 > 8 => 
    right = 8
    j=7
28-

"""