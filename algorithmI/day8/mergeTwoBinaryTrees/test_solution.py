import pytest

from core.dataStructure.TreeNode import to_array
from core.utils.treeNodeConvert import to_binary_tree
from .solution import Solution


@pytest.mark.parametrize("input1, input2, expected",
                         [
                             ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
                             ([1], [1, 2], [2, 2]),
                         ])
def test_number_of_bits(input1, input2, expected):
    root1 = to_binary_tree(input1)
    root2 = to_binary_tree(input2)
    actual = Solution().mergeTrees(root1, root2)
    assert to_array(actual) == expected
