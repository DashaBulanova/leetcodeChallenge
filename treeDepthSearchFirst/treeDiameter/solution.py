# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from core.dataStructure.TreeNode import TreeNode


class Solution:
    def height_and_diameter(self, node: Optional[TreeNode]) -> (int, int):  # heigh длина, max диаметер
        if not node:
            return -1, -1

        if not node.left and not node.right:
            return 0, 0

        left_height, left_diameter = self.height_and_diameter(node.left)
        right_height, right_diameter = self.height_and_diameter(node.right)
        height = max(left_height + 1, right_height + 1)
        current_diameter = left_height + right_height + 2
        return height, max(current_diameter, left_diameter, right_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height_and_diameter(root)[1]

