import pytest

from .solution import Solution


@pytest.mark.parametrize("piles, expected",
                         [
                             ([5, 3, 4, 5], True),
                         ])
def test_number_of_bits(piles, expected):
    actual = Solution().stoneGame(piles)
    assert actual == expected
