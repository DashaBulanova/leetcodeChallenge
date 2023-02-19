# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        result = []
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            if node.right is not None:
                q.append((node.right, level + 1))
            if node.left is not None:
                q.append((node.left, level + 1))

        for i in range(len(result)):
            if i % 2 == 0:
                result[i].reverse()
        return result
