
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _calculate_sum(node, low, high) -> int:
    if node is None:
        return 0

    left_sum = _calculate_sum(node.left, low, high)
    right_sum = _calculate_sum(node.right, low, high)

    if low <= node.val <= high:
        return left_sum + node.val + right_sum
    else:
        return left_sum+right_sum



class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return _calculate_sum(root, low, high)

