import pytest

from core.utils.treeNodeConvert import to_binary_tree
from cousinsInBinaryTree.solution import Solution


@pytest.mark.parametrize("input, x, y, expected",
                         [
                             ([1, 2, 3, 4], 4, 3, False),
                             ([1, 2, 3, None, 4, None, 5], 5, 4, True),
                             ([1, 2, 3, None, 4], 2, 3, False)
                         ])
def test_bst_to_gst(input, x, y, expected):
    root = to_binary_tree(input)

    actual = Solution().isCousins(root, x, y)
    assert actual == expected
