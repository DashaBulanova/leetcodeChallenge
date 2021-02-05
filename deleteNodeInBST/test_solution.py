import pytest

from core.dataStructure.TreeNode import to_bst, to_array
from deleteNodeInBST.solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                             ([5, 3, 6, 2, 4, None, 7], 3, [5, 4, 6, 2, None, None, 7])
                         #    ([5, 3, 6, 2, 4, None, 7],0, [5, 3, 6, 2, 4, None, 7]),
                             #([0], 0, None)
                         ])
def test(input, k, expected):
    input_tree = to_bst(input)
    actual_tree = Solution().deleteNode(input_tree, k)
    actual = to_array(actual_tree)

    assert actual == expected