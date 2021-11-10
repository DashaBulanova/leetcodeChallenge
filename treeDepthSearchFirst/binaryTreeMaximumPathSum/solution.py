# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional, List

from core.dataStructure.TreeNode import TreeNode


class Solution:

    def max_sum_by_path(self, node: Optional[TreeNode]) -> (int, int):  # max dowstream sum by path
        # path, global max sum
        if not node:
            return -math.inf, -math.inf

        if node.left is None and node.right is None:
            return node.val, node.val

        left_path_sum, left_global_max = self.max_sum_by_path(node.left)
        right_path_sum, right_global_max = self.max_sum_by_path(node.right)

        subtree_sum = node.val + max(left_path_sum, 0) + max(right_path_sum, 0)

        left_path_sum = max(left_path_sum, 0) + node.val
        right_path_sum = max(right_path_sum, 0) + node.val

        global_max = max(left_path_sum, right_path_sum, subtree_sum, left_global_max, right_global_max, node.val)

        return max(left_path_sum, right_path_sum, node.val), global_max

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.max_sum_by_path(root)[1]
