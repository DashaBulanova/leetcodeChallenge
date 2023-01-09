# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_array(tree: List[int]) -> Optional[TreeNode]:
    if not tree:
        return None

    root = TreeNode(tree[0])
    q = collections.deque()
    q.append(root)
    for i in range(1, len(tree)):
        if i % 2 == 0:
            node = q.popleft()
            node.right = TreeNode(tree[i]) if tree[i] else None
            curr = node.right
        else:
            node = q[0]
            node.left = TreeNode(tree[i]) if tree[i] else None
            curr = node.left
        if curr:
            q.append(curr)
    return root

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        acc = []
        self.__preorder_traversal(acc, root)
        return acc

    def __preorder_traversal(self, acc, node):
        if not node:
            return

        acc.append(node.val)
        self.__preorder_traversal(acc, node.left)
        self.__preorder_traversal(acc, node.right)
