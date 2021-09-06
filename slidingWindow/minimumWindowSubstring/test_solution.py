import pytest

from .solution import Solution


@pytest.mark.parametrize("input, pattern, expected",
                         [
                             ("ADOBECODEBANC", "ABC", "BANC"),
                             ("a", "aa", ""),
                             ("a", "a", "a"),
                             ("aa", "aa", "aa"),
                             ("cabwefgewcwaefgcf", "cae", "cwae")
                         ])
def test_number_of_bits(input, pattern, expected):
    actual = Solution().minWindow(input, pattern)
    assert actual == expected
