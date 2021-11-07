from core.dataStructure.TreeNode import TreeNode
from .solution import find_path


def test():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    # print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    assert find_path(root, [1, 1, 6]) is True
    assert find_path(root, [1, 6, 5]) is False
    assert find_path(root, [1, 1, 5]) is True
