import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([2, 5, 3, 9, 5, 3], 3),
    ([0], 0)
])
def test(input, expected):
    actual = Solution().minimumAverageDifference(input)
    assert actual == expected
