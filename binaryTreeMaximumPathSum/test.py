import pytest

from .solution import Solution, from_array


@pytest.mark.parametrize("input, expected", [
    # ([1, 2, 3], 6),
    # ([-10, 9, 20, None, None, 15, 7], 42),
    # ([-3], -3),
    # ([2, -1], 2),
    # ([1, -2, 3], 4),
    # ([1, -2, -3, 1, 3, -2, None, -1], 3),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48)
])
def test(input, expected):
    root = from_array(input)
    actual = Solution().maxPathSum(root)
    assert actual == expected
