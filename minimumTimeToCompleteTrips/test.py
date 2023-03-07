import pytest

from .solution import Solution


@pytest.mark.parametrize("time, totalTrips, expected", [
    ([1, 2, 3], 5, 3),
    ([2], 1, 2),
    ([9, 3, 10, 5], 2, 5),
    ([5, 10, 10], 9, 25)
])
def test(time, totalTrips, expected):
    actual = Solution().minimumTime(time, totalTrips)
    assert actual == expected
