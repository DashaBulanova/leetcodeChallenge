from binarySearchTreeToGreaterSumTree.solution import TreeNode, Solution


def test_bst_to_gst():
    tree = TreeNode(4)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(2)
    tree.left.right.right = TreeNode(3)

    tree.right = TreeNode(6)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)
    tree.right.right.right = TreeNode(8)

    actual = Solution().bstToGst(tree)

    assert actual.val == 30

    assert actual.left.val == 36
    assert actual.left._left.val == 36
    assert actual.left._right.val == 35
    assert actual.left._right._right.val == 33

    assert actual.right.val == 21
    assert actual.right._right.val == 15
    assert actual.right._right._right.val == 8
    assert actual.right._right._left is None
    assert actual.right._left.val == 26

