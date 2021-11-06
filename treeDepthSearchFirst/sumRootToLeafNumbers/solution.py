# Definition for a binary tree node.
from typing import Optional

from core.dataStructure.TreeNode import TreeNode


class Solution:
    def is_leaf(self, node: TreeNode):
        return node.left is None and node.right is None

    def sum(self, node: TreeNode, acc_number: str) -> int:
        if node is None:
            return 0

        acc_number = acc_number + str(node.val)
        if self.is_leaf(node):
            return int(acc_number)
        else:
            return self.sum(node.left, acc_number) + self.sum(node.right, acc_number)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root, "")
