import pytest
from .solution import Solution


@pytest.mark.parametrize("word, expected", [
    ("USA", True),
    ("FlaG", False),
    ("leetcode", True),
    ("Google", True)
])
def test(word, expected):
    actual = Solution().detectCapitalUse(word)
    assert actual == expected
