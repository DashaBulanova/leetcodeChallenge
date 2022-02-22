from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []

        def getPath(i, acc):
            if i == len(graph)-1:
                results.append(acc.copy())
                return

            for child in graph[i]:
                acc.append(child)
                getPath(child, acc)
                del acc[-1]

        acc = [0]
        getPath(0, acc)
        return results
