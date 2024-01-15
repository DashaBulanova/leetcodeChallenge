class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players_balance = {}
        for match in matches:
            players_balance[match[0]] = players_balance.get(match[0],0)
            players_balance[match[1]] = players_balance.get(match[1],0) - 1

        return [
            sorted([k for k,v in players_balance.items() if v == 0]), 
            sorted([k for k,v in players_balance.items() if v == -1])
        ]
