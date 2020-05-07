from core.utils.treeNodeConvert import to_binary_tree


def test_to_binary_tree():
    input = [1, 2, 3, 4]
    actual = to_binary_tree(input)
    assert actual.val == 1
    assert actual.left.val == 2
    assert actual.right.val == 3
    assert actual.left.left.val == 4


def test_to_binary_tree_2():
    input = [1, 2, 3, None, 4, None, 5]
    actual = to_binary_tree(input)
    assert actual.val == 1
    assert actual.left.val == 2
    assert actual.left.left is None
    assert actual.left.right.val == 4
    assert actual.right.val == 3
    assert actual.right.left is None
    assert actual.right.right.val == 5

