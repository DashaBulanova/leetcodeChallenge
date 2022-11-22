import collections
import dataclasses
from typing import List


@dataclasses.dataclass
class TreeNode:
    value: int
    level: int


class Solution:
    def __fill_squares(self, n: int) -> List[int]:
        perfect_squares = []
        for i in range(1, n+1):
            square = i * i
            if square <= n:
                perfect_squares.append(square)
            else:
                break
        return perfect_squares

    def numSquares(self, n: int):
        perfect_squares = self.__fill_squares(n)

        root = TreeNode(value=n, level=0)
        nodes = set()
        stack = collections.deque([root])

        while stack:
            node = stack.popleft()

            for i in range(len(perfect_squares)-1, -1, -1):
                sq = perfect_squares[i]
                if node.value - sq < 0:
                    continue
                elif node.value - sq == 0:
                    return node.level + 1
                else:
                    if node.value - sq not in nodes:
                        stack.append(TreeNode(node.value - sq, node.level + 1))
                        nodes.add(node.value - sq)
