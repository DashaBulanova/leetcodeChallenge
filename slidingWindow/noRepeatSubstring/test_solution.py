import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ("aabccbb", 3),
                             ("abbbb", 2),
                             ("abccde", 3),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().non_repeat_substring(input)
    assert actual == expected
