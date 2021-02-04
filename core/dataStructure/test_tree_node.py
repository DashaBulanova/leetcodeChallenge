from core.dataStructure.TreeNode import to_bst


def test_to_bst():
    input = [3, 1, 4, None, 2]
    actual = to_bst(input)

    assert actual.val == 3
    assert actual.left is not None
    assert actual.left.val == 1
    assert actual.right is not None
    assert actual.right.val == 4
    assert actual.left.left is None
    assert actual.left.right is not None
    assert actual.left.right.val == 2
    assert actual.right.left is None
    assert actual.right.right is None
    assert actual.left.right.left is None
    assert actual.left.right.right is None
