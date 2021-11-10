import pytest

from core.utils.treeNodeConvert import to_binary_tree
from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 2, 3], 6),
                             ([10, 9, 20, None, None, 15, 7], 54),
                             ([-10, 9, 20, None, None, 15, 7], 42),
                             ([2, -1], 2),
                             ([-3], -3),
                             ([2, -1, -2], 2),
                             ([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6], 16)
                         ])
def test(input, expected):
    tree = to_binary_tree(input)
    actual = Solution().maxPathSum(tree)
    assert actual == expected
