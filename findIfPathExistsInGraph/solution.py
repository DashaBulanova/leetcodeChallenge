import collections


class Solution:
    class UnionFind:

        def __init__(self, n):
            self._parents = list(range(0, n))

        def find(self, p):
            while (p != self._parents[p]):
                p = self._parents[p]
            return p

        def union(self, p, q):
            root_p, root_q = self.find(p), self.find(q)
            self._parents[root_p] = root_q

        def connected(self, p, q):
            return self.find(p) == self.find(q)

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        uf = self.UnionFind(n)

        for u, v in edges:
            uf.union(u, v)
        return uf.connected(source, destination)


"""
 [0, 1], [0, 2], [2, 4], [5, 4], [4, 3]
 i=0 u=0, v=1
 q=1

 i=1 u=0, v=2
 q=1,2

i=2 u=2, v=4
 q=1,4

i=3 u=5, v=4
q=1,5


"""
