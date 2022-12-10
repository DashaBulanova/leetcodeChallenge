import pytest
from .solution import Solution, TreeNode, from_array


@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3, 4, 5, 6], 110),
    ([1, None, 2, 3, 4, None, None, 5, 6], 90)
])
def test(input, expected):
    head = from_array(input)
    actual = Solution().maxProduct(head)
    assert actual == expected
