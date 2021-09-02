import pytest

from .solution import Solution


@pytest.mark.parametrize("input, s, expected",
                         [
                             ("araaci", 2, 4),
                             ("araaci", 1, 2),
                             ("cbbebi", 3, 5),
                             ("cbbebi", 10, 6),
                         ])
def test_number_of_bits(input, s, expected):
    actual = Solution().longest_substring_with_k_distinct(input, s)
    assert actual == expected
