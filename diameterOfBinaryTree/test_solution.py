from trimBinarySearchTree.solution import TreeNode, Solution


def test_case_1():
    tree = TreeNode(1)
    tree.left = TreeNode(0)
    tree.right = TreeNode(2)

    actual = Solution().trimBST(tree, 1, 2)

    assert actual.val == 1
    assert actual.left is None
    assert actual.right.val == 2
    assert actual.right.right is None
    assert actual.right.left is None


def test_case_2():
    tree = TreeNode(3)
    tree.left = TreeNode(0)
    tree.left.right = TreeNode(2)
    tree.left.right.left = TreeNode(1)
    tree.right = TreeNode(4)

    actual = Solution().trimBST(tree, 1, 3)

    assert actual.val == 3
    assert actual.right is None
    assert actual.left.val == 2
    assert actual.left.left.val == 1
    assert actual.left.right is None
