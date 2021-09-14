import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([-3, 0, 1, 2, -1, 1, -2], [[-3, 2, 1], [-2, 2, 0], [-2, 1, 1], [-1, 1, 0]]),
                             ([-5, 2, -1, -2, 3], [[-5, 3, 2], [-2, 3, -1]]),
                             ([-5, -2, -1, 0, 0, 0, 1], [[-1, 1, 0], [0, 0, 0]]),
                         ])
def test(input, expected):
    actual = Solution().search_triplets(input)
    assert actual == expected