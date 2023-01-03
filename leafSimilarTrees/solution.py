import collections
from typing import Optional

from core.exceptions.constraints_violation import ConstraintsViolationException


def from_array(arr: list[int]):
    if not arr:
        raise ConstraintsViolationException()

    nodes = collections.deque()
    root = None
    for i in range(len(arr)):
        current = TreeNode(arr[i]) if arr[i] else None

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
        return self.maxAncestorDiff(root, None, None)

    def maxDifference(self, node, head, ancestor) -> int:
        if not node:
            return 0

        diff = 0
        if not ancestor:
            diff = max(
                abs(node.val - head.val),
                abs(node.val - ancestor.val))
        elif not head:
            diff = max(
                abs(node.val - head.val))

        left_max = self.maxDifference(node.left, head=node, ancestor=head)
        right_max = self.maxDifference(node.right, head=node, ancestor=head)

        return max(left_max, right_max, diff)
