import pytest

from solution import Solution


@pytest.mark.parametrize("first, second, expected",
                         [
                             ([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]],
                              [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
                             ([[1, 3], [5, 9]], [], []),
                             ([], [[4, 8], [10, 12]], []),
                             ([[1, 7]], [[3, 10]], [[3, 7]]),
                             ([[8, 15]], [[2, 6], [8, 10], [12, 20]], [[8, 10], [12, 15]]),
                             ([[3, 5], [9, 20]], [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]],
                              [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]])
                         ])
def test(first, second, expected):
    actual = Solution().intervalIntersection(first, second)
    assert actual == expected
