import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
                             ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]),
                         ])
def test(input, expected):
    actual = Solution().make_squares(input)
    assert actual == expected
