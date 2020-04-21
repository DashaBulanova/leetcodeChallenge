import pytest

from leftColumnWithAtLeastAOne.solution import BinaryMatrix, Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([[0, 0], [1, 1]], 0),
                             ([[0, 0], [0, 1]], 1),
                             ([[0, 0], [0, 0]], -1),
                             ([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]], 1)
                         ])
def test_solution(input, expected):
    actual = Solution().leftMostColumnWithOne(BinaryMatrix(input))
    assert actual == expected
