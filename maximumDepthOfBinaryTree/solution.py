from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depth(node: TreeNode) -> int:
            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            return max(left_depth, right_depth) + 1

        return depth(root)
