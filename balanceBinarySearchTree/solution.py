# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure import TreeNode

class Solution:

    heights = dict()

    def set_height(self, node: TreeNode, height: int):
        self.heights[node.val] = height

    def get_height(self, node: TreeNode) -> int:
        if node is None:
            return -1

        return self.heights[node.val]

    def update_height(self, node):
        self.heights[node.val] = max(self.get_height(node.right), self.get_height(node.left)) + 1

    def right_heavy(self, node):
        return self.get_height(node.right) > self.get_height(node.left) + 1

    def left_heavy(self, node):
        return self.get_height(node.left) > self.get_height(node.right) + 1

    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.rebalance(root)

    def rebalance(self, node: TreeNode) -> TreeNode:
        if node is None:
            return None

        node.left = self.rebalance(node.left)
        node.right = self.rebalance(node.right)

        if self.right_heavy(node):
            if self.get_height(node.right.left) > self.get_height(node.right.right):
                node.right = self.right_rotate(node.right)
            node = self.rebalance(self.left_rotate(node))
        elif self.left_heavy(node):
            if self.get_height(node.left.right) > self.get_height(node.left.left):
                node.left = self.left_rotate(node.left)
            node = self.rebalance(self.right_rotate(node))

        self.update_height(node)
        return node

    def left_rotate(self, node: TreeNode) -> TreeNode:
        root = node.right
        node.right = root.left
        root.left = node
        return root

    def right_rotate(self, node: TreeNode) -> TreeNode:
        root = node.left
        node.left = root.right
        root.right = node
        return root
