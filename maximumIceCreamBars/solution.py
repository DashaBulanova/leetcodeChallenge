class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        result = 0

        for i in range(len(costs)):
            coins -= costs[i]
            result += 1 if coins >= 0 else 0

            if coins <= 0:
                return result

        return result


"""
[1,1  2,3 4]
i=0
coins=7-1=6
r=1

i=1 coins=5 r=2
i=2 coins=3 r=3
i=3 coins
"""
