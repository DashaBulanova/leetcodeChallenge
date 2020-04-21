# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.__sum = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        root.right = self.bstToGst(root.right)

        self.__sum += root.val
        root.val = self.__sum

        root.left = self.bstToGst(root.left)

        return root
