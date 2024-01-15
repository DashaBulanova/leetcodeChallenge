class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = {}
        all_losers = {}
        for match in matches:
            winners[match[0]] = winners.get(match[0], 0) + 1
            all_losers[match[1]] = all_losers.get(match[1],0) + 1

        return [
            sorted(set(winners.keys())-set(all_losers.keys())), 
            sorted([k for k,v in all_losers.items() if v == 1])
        ]
