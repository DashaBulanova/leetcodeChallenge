# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure import TreeNode
class SubTree:
    def __init__(self,
                 is_valid: bool,
                 max_sum: int,
                 min_item: int = None,
                 max_item: int = None):
        self.min_item = min_item
        self.max_item = max_item
        self.max_sum = max_sum
        self.is_valid = is_valid


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self._bst_sum(root)
        return self.max_sum

    max_sum = 0

    def _bst_sum(self, node: TreeNode) -> SubTree:
        if node is None:
            return SubTree(True, 0)

        if node.left is None and node.right is None:
            self.max_sum = max(node.val, self.max_sum)
            return SubTree(True, node.val, node.val, node.val)

        left_subtree = self._bst_sum(node.left)
        right_subtree = self._bst_sum(node.right)

        if self._is_valid(node, left_subtree, right_subtree):
            sum = left_subtree.max_sum + right_subtree.max_sum + node.val
            self.max_sum = max(sum, self.max_sum)
            return SubTree(True, sum,
                           left_subtree.min_item if left_subtree.min_item is not None else node.val,
                           right_subtree.max_item if right_subtree.max_item is not None else node.val)
        else:
            return SubTree(False, 0)

    def _is_valid(self, node: TreeNode, left_subtree: SubTree, right_subtree: SubTree) -> bool:
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is None:
            return (node.val > node.left.val and
                    left_subtree.is_valid and
                    left_subtree.max_item < node.val)

        if node.right is not None and node.left is None:
            return node.val < node.right.val and right_subtree.is_valid and right_subtree.min_item > node.val

        return (node.left.val < node.val < node.right.val and
                left_subtree.is_valid and
                right_subtree.is_valid and
                left_subtree.max_item < node.val < right_subtree.min_item)
