import pytest

from core.utils.treeNodeConvert import to_binary_tree
from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([1, 2, 3, 4, 5], 3),
                          ([1, 2], 1)])
def test(input, expected):
    tree = to_binary_tree(input)
    actual = Solution().diameterOfBinaryTree(tree)
    assert actual == expected
