# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        result = []
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)

            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))

        return result
