import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
])
def test(input, expected):
    actual = Solution().dailyTemperatures(input)
    assert actual == expected
