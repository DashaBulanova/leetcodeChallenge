# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        return self._sum(root, low, high)
    def _sum(self, node:TreeNode, low, high) -> int:
        if node is None:
            return 0

        result = 0
        if node.val < high:
            result += self._sum(node.right, low, high)
        if node.val > low:
            result += self._sum(node.left, low, high)

        if low <= node.val <= high:
            result +=  node.val

        return result
