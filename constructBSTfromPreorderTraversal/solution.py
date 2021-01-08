class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class BinarySearchTree:

    def __init__(self):
        self.__root__ = None

    def insert(self, val):
        """
        :param val:
        """
        if self.__root__ is None:
            self.__root__ = TreeNode(val)
        else:
            self.__root__ = self.inner_insert(val, self.__root__)

    def inner_insert(self, val, node):
        """

        :param val: int
        :type node: TreeNode
        """
        if node is None:
            return TreeNode(val)
        else:
            if val >= node.val:
                node.right = self.inner_insert(val, node.right)
            else:
                node.left = self.inner_insert(val, node.left)
            return node

    def preorder(self):
        result = []
        self.breadth_traversal(self.__root__, result)
        return result

    def breadth_traversal(self, node, result):
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            self.breadth_traversal(node._left, result)
            self.breadth_traversal(node._right, result)



class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        bst = BinarySearchTree()
        for value in preorder:
            bst.insert(value)

        return bst.preorder()


