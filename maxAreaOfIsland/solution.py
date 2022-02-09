from typing import List


class UnionFind:

    def __init__(self, grid: List[List[int]]):
        self.m = len(grid)
        self.n = len(grid[0])
        self.ids = [0] * self.m * self.n

        for i in range(len(self.ids)):
            self.ids[i] = i

        self.sz = [0] * self.m * self.n
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.sz[self.get_index(i, j)] = grid[i][j]

    def get_index(self, i, j):
        return i * self.n + j

    def root(self, i):
        curr = i
        while curr != self.ids[curr]:
            curr = self.ids[curr]
        return curr

    def union(self, i, j, i1, j1):
        p = self.get_index(i, j)
        q = self.get_index(i1, j1)

        r1 = self.root(p)
        r2 = self.root(q)
        if r1 != r2:
            if self.sz[r1] >= self.sz[r2]:
                self.ids[r2] = r1
                self.sz[r1] += self.sz[r2]
            else:
                self.ids[r1] = r2
                self.sz[r2] += self.sz[r1]

    def get_max_island(self):
        return max(self.sz)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        uf = UnionFind(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i < m - 1 and grid[i + 1][j] == 1:
                        uf.union(i, j, i + 1, j)
                    if j < n - 1 and grid[i][j + 1] == 1:
                        uf.union(i, j, i, j + 1)

        res = uf.get_max_island()
        return res
