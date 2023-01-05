import pytest
from .solution import Solution


@pytest.mark.parametrize("points, expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[-3, -1], [10, 16], [2, 8], [1, 6], [7, 12]], 3),
    ([[-3, -1], [10, 16], [-2, 8], [1, 6], [7, 12]], 3),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
])
def test(points, expected):
    actual = Solution().findMinArrowShots(points)
    assert actual == expected
