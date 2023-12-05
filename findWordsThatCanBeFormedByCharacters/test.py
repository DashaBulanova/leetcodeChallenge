import pytest
from .solution import Solution

@pytest.mark.parametrize("words, chars, expected", [
(["cat","bt","hat","tree"],"atach", 6),
(["hello","world","leetcode"], "welldonehoneyr",10)
    ])
def test(words, chars, expected):
    actual = Solution().countCharacters(words, chars)
    assert actual == expected
