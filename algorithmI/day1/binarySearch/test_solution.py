import pytest

from .solution import Solution


@pytest.mark.parametrize("input,  target, expected",
                         [
                             ([-1, 0, 3, 5, 9, 12], 9, 4),
                             ([-1, 0, 3, 5, 9, 12], 2, -1),
                             ([5], 5, 0),
                         ])
def test_number_of_bits(input, target, expected):
    actual = Solution().search(input, target)
    assert actual == expected
