class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []

        def get_path(index, res):
            if index == len(graph) - 1:
                return res.append(index)
            if graph[index] == []:
                return []

            res = []
            for i in graph[index]:
                res.append(i)
                r = get_path(i, graph[i])
                res.append(r)

        get_path(0, len(graph), graph[0])
        return res


"""[[1, 2], [3], [3], []]
[1, 2]

__go_deep: 0, [1, 2]
i = 1 go_deep(1, [3])=3 -> 1
    go_deep(3, graph[3]) -> 3
"""
