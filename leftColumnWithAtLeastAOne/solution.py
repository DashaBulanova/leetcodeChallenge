# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class BinaryMatrix(object):

    def __init__(self, mat: List[int]):
        self.mat = mat

    def get(self, x: int, y: int) -> int:
        return self.mat[x][y]

    def dimensions(self) -> List[int]:
        res = [len(self.mat), len(self.mat[0])]
        return res


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimen = binaryMatrix.dimensions()
        n, m = dimen[0], dimen[1]

        max = -1
        i = 0
        j = m - 1
        while i < n and j >= 0:
            value = binaryMatrix.get(i, j)
            if value == 1:
                max = j
                j -= 1
            else:
                i += 1

        return max
