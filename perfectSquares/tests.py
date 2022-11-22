import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (12, 3),
                             (13, 2),
                             (16, 1),
                             (1, 1),
                             (1243, 3),
                             (7168, 4)
                         ])
def test(input, expected):
    actual = Solution().numSquares(input)
    assert actual == expected
