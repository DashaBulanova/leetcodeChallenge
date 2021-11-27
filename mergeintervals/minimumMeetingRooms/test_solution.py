import pytest

from solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([[0, 30], [5, 10], [15, 20]], 2),
                             ([[7, 10], [2, 4]], 1),
                             ([[1, 4], [2, 5], [7, 9]], 2),
                             ([[6, 7], [2, 4], [8, 12]], 1),
                             ([[1, 4], [2, 3], [3, 6]], 2),
                             ([[4, 5], [2, 3], [2, 4], [3, 5]], 2)
                         ])
def test(input, expected):
    actual = Solution().minMeetingRooms(input)
    assert actual == expected
