import pytest

from checkIfItIsAStraightLine.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
                             ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
                             ([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]], False),
                         ])
def test_solution(input, expected):
    actual = Solution().checkStraightLine(input)
    assert actual == expected
