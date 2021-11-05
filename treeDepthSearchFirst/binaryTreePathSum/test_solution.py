import pytest

from .solution import has_path, TreeNode


@pytest.mark.parametrize("target, expected",
                         [(23, True),
                          (16, False),
                          (18, True),
                          (14, False)])
def test(target, expected):
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    assert has_path(root, target) == expected
