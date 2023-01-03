import collections
from typing import Optional

from core.exceptions.constraints_violation import ConstraintsViolationException


def from_array(arr: list[int]):
    if not arr:
        raise ConstraintsViolationException()

    nodes = collections.deque()
    root = None
    for i in range(len(arr)):
        current = TreeNode(arr[i]) if arr[i] is not None else None

        if i == 0:
            root = current
        elif i % 2 == 0:
            node = nodes.popleft()
            node.right = current
        else:
            node = nodes[0]
            node.left = current

        if current:
            nodes.append(current)

    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.maxDifference(root)

    def maxDifference(self, node) -> int:
        if not node:
            return 0

        diff = 0

        left_max = self.maxDifference(node.left)
        right_max = self.maxDifference(node.right)

        if node.left and node.right:
            diff = max(abs(node.val - node.left.val), abs(node.val - node.right.val))
        elif node.left:
            diff = abs(node.val - node.left.val)
        elif node.right:
            diff = abs(node.val - node.right.val)

        return max(left_max, right_max, diff)
