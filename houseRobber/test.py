import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([2, 7, 9, 3, 1], 12),
    ([1, 2, 3, 1], 4),
    ([6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3], 39),
    ([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
      185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211], 3365)
])
def test(input, expected):
    actual = Solution().rob(input)
    assert actual == expected
