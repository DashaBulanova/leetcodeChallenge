# class TreeNode:


# def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure.TreeNode import TreeNode


class BSTNode(TreeNode):
    def __init__(self, parent=None, val=0):
        super(BSTNode, self).__init__(val)
        self.parent = parent
        self.height = 0

    def insert(self):


class BST:
    root: TreeNode = None

    def insert(self, val) -> TreeNode:
        if self.root is None:
            self.root = BSTNode(None, val)
            return self.root
        else:
            return self._insert(val, self.root)

    def _insert(self, val, current: TreeNode) -> TreeNode:
        if current is None:
            raise ValueError()

        if val > current.val:
            if current.right is None:
                node = BSTNode(current, val)
                current.right = node
                return node
            else:
                return self._insert(val, current.right)
        else:
            if current.left is None:
                node = BSTNode(current, val)
                current.left = node
                return node
            else:
                return self._insert(val, current.left)


class AVLTree(BST):
    height: int = 0

    def find(self):
        pass

    def insert(self, val):
        node = super(AVLTree, self).insert(val)
        self.rebalance(node)

    def rebalance(self, node):
        pass

    def delete(self):
        pass

    # def __str__(self):
    #     #in-order traversal
