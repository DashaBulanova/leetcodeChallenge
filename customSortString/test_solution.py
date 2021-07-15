import pytest

from customSortString.solution import Solution


@pytest.mark.parametrize("order, sample, expected",
                         [
                             ("cba", "abcd", "cbad")])
def test_number_of_bits(order, sample, expected):
    actual = Solution().customSortString(order, sample)
    assert actual == expected
