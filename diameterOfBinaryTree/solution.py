# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        """
        :type x: int
        :type left: TreeNode
        :type right: TreeNode
        """
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return None
        

