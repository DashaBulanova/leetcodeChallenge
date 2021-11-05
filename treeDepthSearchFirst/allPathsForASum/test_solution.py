import pytest

from .solution import find_paths, TreeNode


@pytest.mark.parametrize("target, expected", [
    (12, [[1, 7, 4], [1, 9, 2]])
])
def test(target, expected):
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    assert find_paths(root, target) == expected
