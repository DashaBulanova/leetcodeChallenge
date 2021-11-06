import pytest

from .solution import Solution


@pytest.mark.parametrize("image, sr, sc, newColor, expected",
                         [
                             ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
                             ([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),
                             ([[0, 0, 0], [0, 1, 1]], 1, 1, 1,[[0, 0, 0], [0, 1, 1]] )
                         ])
def test_number_of_bits(image, sr, sc, newColor, expected):
    actual = Solution().floodFill(image, sr, sc, newColor)
    assert actual == expected
