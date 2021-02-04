import pytest

from core.dataStructure.TreeNode import to_bst
from kthSmallestElementInAbst.solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                            # ([3, 1, 4, None, 2], 1, 1),
                            # ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
                             ([5, 3, 6, 2, 4, None, None, 1], 6, 6)
                         ])
def test(input, k, expected):
    input_tree = to_bst(input)
    actual = Solution().kthSmallest(input_tree, k)

    assert actual == expected