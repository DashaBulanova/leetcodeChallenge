import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ("abcabcbb", 3),
                             ("bbbbb", 1),
                             ("pwwkew", 3),
                             ("", 0),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().lengthOfLongestSubstring(input)
    assert actual == expected
