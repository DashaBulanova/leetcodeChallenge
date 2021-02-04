# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure import TreeNode


class Solution:
    _parents = dict()

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self._parents[root] = None
        current = self._find_min(root)
        i = 1
        while i < k:
            current = self._successor(current)
            i += 1

        return current.val

    def _find_min(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node
        self._parents[node.left] = node
        return self._find_min(node.left)

    def _successor(self, node: TreeNode) -> TreeNode:
        #есть правое поддерево
        if node.right is not None:
            self._parents[node.right] = node
            return self._find_min(node.right)
        #правого поддерева нету, значт нужно подняться на самый верх по правой бранче до головы
        current = node
        while self._parents[current] is not None and current == self._parents[current].right:
            current = self._parents[current]
        return self._parents[current]
