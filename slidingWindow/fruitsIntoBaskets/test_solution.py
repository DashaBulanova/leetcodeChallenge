import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (['A', 'B', 'C', 'A', 'C'], 3),
                             (['A', 'B', 'C', 'B', 'B', 'C'], 5),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().fruits_into_baskets(input)
    assert actual == expected
