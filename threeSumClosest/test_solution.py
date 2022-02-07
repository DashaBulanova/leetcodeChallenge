import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected", [
    ([-1, 2, 1, -4], 1, 2),
    ([0, 0, 0], 1, 0),
    ([1, 2, 4, 8, 16, 32, 64, 128], 82, 82)
])
def test(input, target, expected):
    actual = Solution().threeSumClosest(input, target)
    assert actual == expected
