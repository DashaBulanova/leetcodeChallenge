import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_array(input: list[int]) -> TreeNode:
    root = None
    q = collections.deque()
    for i in range(len(input)):
        curr = TreeNode(input[i]) if input[i] is not None else None
        if i == 0:
            root = curr
        elif i % 2 == 0:
            node = q.popleft()
            node.right = curr
        else:
            node = q[0]
            node.left = curr
        if curr is not None:
            q.append(curr)
    return root


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.__calculateMax(root)[1]

    def __calculateMax(self, node: TreeNode) -> (int, int):
        if node is None:
            return None, None

        left = self.__calculateMax(node.left)
        right = self.__calculateMax(node.right)
        curr = node.val
        path = []
        if left[0] is not None:
            path.append(left[1])
            path.append(node.val + left[0])
            curr += left[0]
        if right[0] is not None:
            path.append(right[1])
            path.append(node.val + right[0])
            curr += right[0]

        path.append(curr)
        path.append(node.val)
        return curr, max(path)
