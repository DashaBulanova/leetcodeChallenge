class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        teams = n
        while teams>=2:
            matches += teams//2
            teams = teams//2 + teams%2
        return matches

"""
n=7
m=0
t=7//2=3+1=4
matches=3

t=4
matches=3+2
teams=2
t=2
matches=3+2+1
"""
