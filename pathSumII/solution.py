# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from core.dataStructure.TreeNode import TreeNode


def is_leaf(node):
    return node.left is None and node.right is None


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []
        self.sum(root, targetSum, 0, result, [])
        return result

    def sum(self,
            node: TreeNode,
            targetSum: int,
            accumSum: int,
            result: List[List[int]],
            path_accum: List[int]):
        if node is None:
            return result

        accum_sum = node.val + accumSum
        path_accum.append(node.val)

        if is_leaf(node):
            if accum_sum == targetSum:
                result.append(list(path_accum))

            path_accum.pop(len(path_accum)-1)
        else:
            self.sum(node.left, targetSum, accum_sum, result, path_accum)
            self.sum(node.right, targetSum, accum_sum, result, path_accum)
            path_accum.pop(len(path_accum)-1)




