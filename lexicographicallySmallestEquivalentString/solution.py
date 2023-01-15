import dataclasses


@dataclasses.dataclass
class Node:
    parent: str
    val: str


class UnionFind:
    def __init__(self, n: int):
        self.id = [0] * n
        for i in range(n):
            self.id[i] = i

    def find(self, x) -> int:
        c = x
        while self.id[c] != c:
            c = self.id[c]
        return c

    def connected(self, x, y) -> bool:
        return self.id[x] == self.id[y]

    def union(self, x, y):
        xid, yid = self.find(x), self.find(y)
        if xid < yid:
            self.id[yid] = xid
        else:
            self.id[xid] = yid

    def get_id(self, x) -> int:
        return self.find(x)

"""
hdld
a b c d e f g h i j k  l  m  n  o p  q  r  s  t  u  v  w x  y  z
0 1 2 3 4 5 6 7 8 9 10 11 12 13 3 15 16 11 18 19 20 21 7 23 24 25
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # alphabet: [97-122] = 26
        uf = UnionFind(26)
        for i in range(len(s1)):
            c1 = ord(s1[i]) - 97
            c2 = ord(s2[i]) - 97
            if not uf.connected(c1, c2):
                uf.union(c1, c2)

        res = []
        for c in baseStr:
            p = uf.get_id(ord(c) - 97)
            res.append(chr(p + 97))
        return ''.join(res)
