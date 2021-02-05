# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure import TreeNode


class Solution:
    _parents = dict()

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self._parents[root] = None

        node = self._find(root, key)
        if node is not None:
            return self._delete(root, node)
        return root

    def _find(self, node: TreeNode, key):
        if node is None:
            return None

        if node.val == key:
            return node
        if key > node.val:
            self._parents[node.right] = node
            return self._find(node.right, key)

        if key < node.val:
            self._parents[node.left] = node
            return self._find(node.left, key)

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

    def _delete(self, root: TreeNode, node: TreeNode):
        if node is None:
            raise Exception()

        parent = self._parents[node]
        if node.left is None and node.right is None:
            if parent is None:
                return None
            elif parent.left == node:
                parent.left = None
                return root
            else:
                parent.right = None
                return root

        elif node.left is not None and node.right is None:
            if parent is None:
                return node.left
            if parent.left == node:
                parent.left = node.left
                return root
            else:
                parent.right = node.left
                return root

        elif node.right is not None and node.left is None:
            if parent is None:
                return node.right
            if parent.left == node:
                parent.left = node.right
                return root
            else:
                parent.right = node.right
                return root

        else:
            next_larger = self._successor(node)
            node.val, next_larger.val = next_larger.val, node.val
            return self._delete(root, next_larger)
