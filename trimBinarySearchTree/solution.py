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

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)

        else:
            if root.val > R:
                root = self.trimBST(root.left, L, R)
            elif root.val < L:
                root = self.trimBST(root.right, L, R)

        return root

