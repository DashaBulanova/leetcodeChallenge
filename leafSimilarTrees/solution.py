from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _define_leaf(self, node, acc):
        if node is None:
            return

        if node.left is None and node.right is None:
            acc.append(node.val)
            return

        if node.left is not None:
            self._define_leaf(node.left, acc)
        if node.right is not None:
            self._define_leaf(node.right, acc)
        return

    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is None:
            return False
        if root1 is None and root2 is not None:
            return False

        leaf_1: list = []
        self._define_leaf(root1, leaf_1)

        leaf_2: list = []
        self._define_leaf(root2, leaf_2)

        return leaf_1 == leaf_2



