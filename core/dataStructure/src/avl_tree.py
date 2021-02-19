# class TreeNode:


# def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure.TreeNode import TreeNode


#       43
#
#   4           6
#2      4   4       4
class AVLTree:
    root: TreeNode = None
    height: int = 0

    def find(self):
        pass

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert(val, self.root)

    def __insert(self, val, node: TreeNode):
        if val <= node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.__insert(val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.__insert(val, node.right)

    def delete(self):
        pass

    # def __str__(self):
    #     #in-order traversal


