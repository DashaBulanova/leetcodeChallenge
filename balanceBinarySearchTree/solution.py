# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import enum
from enum import Enum

from core.dataStructure import TreeNode


def height(node) -> int:
    pass


def right_heavy(left_height, right_height):
    return right_height > left_height + 1


def left_heavy(left_height, right_height):
    return left_height > right_height + 1


class Balance(enum.IntEnum):
    NONE = -1
    EVEN = 0
    LEFT_HEAVY = 1
    RIGHT_HEAVY = 2

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.balance(root)[0]

    def balance(self, node: TreeNode) -> (TreeNode, Balance, int):
        if node is None:
            return None, Balance.NONE, -1

        if node.left is None and node.right is None:
            return node, Balance.EVEN, 0

        node.left, left_balance, left_height = self.balance(node.left)
        node.right, right_balance, right_height = self.balance(node.right)

        if left_height == right_height:
            return node, Balance.EVEN, left_height+1

        if left_height == right_height + 1:
            return node, Balance.LEFT_HEAVY, left_height + 1

        if right_height == left_height + 1:
            return node, Balance.RIGHT_HEAVY, right_height + 1

        if right_heavy(left_height, right_height):
            if right_balance == Balance.LEFT_HEAVY:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node), Balance.EVEN, right_height
        if left_heavy(left_height, right_height):
            if left_balance == Balance.RIGHT_HEAVY:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node), Balance.EVEN, left_height

    def left_rotate(self, node: TreeNode) -> TreeNode:
        root = node.right
        node.right = None
        node.right = root.left
        root.left = node
        return self.balance(root)[0]

    def right_rotate(self, node) -> TreeNode:
        root = node.left
        node.left = None
        node.left = root.right
        root.right = node
        return self.balance(root)[0]
