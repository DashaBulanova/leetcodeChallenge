import pytest

from core.dataStructure.TreeNode import to_bst
from maximumSumBstInBinaryTree.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6], 20),
                             ([4, 3, None, 1, 2], 2),
                             ([-4, -2, -5], 0),
                             ([2, 1, 3], 6),
                             ([5, 4, 8, 3, None, 6, 3], 7),
                             ([4, 8, None, 6, 1, 9, None, -5, 4, None, None, None, -3, None, 10], 14),
                             ([4, 3, 8, 3, None, None, 7, 1, 4, None, 6, None, None, None, 5, 10], 13)
                         ])
def test(input, expected):
    input_tree = to_bst(input)
    actual = Solution().maxSumBST(input_tree)

    assert actual == expected