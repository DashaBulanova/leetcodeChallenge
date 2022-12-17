import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ("the sky is blue", "blue is sky the"),
    ("the sky is blue  e", "e blue is sky the"),
    ("  hello world  ", "world hello")
])
def test(input, expected):
    actual = Solution().reverseWords(input)
    assert actual == expected
