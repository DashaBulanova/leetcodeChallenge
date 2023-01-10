# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create(cls, arr: List[int]) -> "TreeNode":
        q = collections.deque()
        root = TreeNode(arr[0])
        q.append(root)

        for i in range(1, len(arr)):
            curr = TreeNode(arr[i]) if arr[i] else None
            if i % 2 == 0:
                node = q.popleft()
                node.right = curr
            else:
                node = q[0]
                node.left = curr
            if curr:
                q.append(curr)
        return root


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.__is_the_same(p, q)

    def __is_the_same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        if not p and q:
            return False
        if p is None and q is None:
            return True

        if p.val != q.val:
            return False
        left = self.__is_the_same(p.left, q.left)
        right = self.__is_the_same(p.right, q.right)

        return left and right
