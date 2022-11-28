from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # identifier of player: [0, 1] 0- count of winning games 1 - number of losing games
        players = {}

        for match in matches:
            if match[0] not in players:
                players[match[0]] = 0
            if match[1] in players:
                players[match[1]] += 1
            else:
                players[match[1]] = 1

        result_winner = []
        result_loser = []
        for i in sorted(players.keys()):
            if players[i] == 0:
                result_winner.append(i)
            if players[i] == 1:
                result_loser.append(i)

        return [result_winner, result_loser]
