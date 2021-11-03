import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
                             ("God Ding","doG gniD")
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().reverseWords(input)
    assert actual == expected
