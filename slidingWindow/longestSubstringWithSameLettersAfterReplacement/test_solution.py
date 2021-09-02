import pytest

from .solution import Solution


@pytest.mark.parametrize("input, s, expected",
                         [
                             # ("aabccbb", 2, 5),
                             # ("abbcb", 1, 4),
                             # ("abccde", 1, 3),
                             ("aaabbbbccc", 2, 7),
                         ])
def test_number_of_bits(input, s, expected):
    actual = Solution().length_of_longest_substring1(input, s)
    assert actual == expected
