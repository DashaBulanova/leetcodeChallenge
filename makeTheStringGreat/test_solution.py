import pytest
from makeTheStringGreat.solution import Solution


@pytest.mark.parametrize("input, expected", [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s")
])
def test(input, expected):
    actual = Solution().makeGood(input)
    assert actual == expected
