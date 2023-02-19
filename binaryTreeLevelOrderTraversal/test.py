import pytest

from binaryTreeZigzagLevelOrderTraversal.test import __from_array
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
])
def test(input, expected):
    root = __from_array(input)
    actual = Solution().levelOrder(root)
    assert actual == expected
