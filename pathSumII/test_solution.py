import pytest

from core.dataStructure.TreeNode import to_bst
from .solution import Solution


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
                             ([1, 2, 3], 5, []),
                             ([1, 2], 1, [])
                         ])
def test_number_of_bits(input, target, expected):
    root = to_bst(input)
    actual = Solution().pathSum(root, target)
    assert actual == expected
