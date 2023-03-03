import pytest
from .solution import Solution

@pytest.mark.parametrize("haystack, needle, expected", [
	("sadbutsad", "sad", 0),
	("aaaba", "aaba", 1),
	("leetcode", "leeto", -1)
])
def test(haystack, needle, expected):
	actual = Solution().strStr(haystack, needle)
	assert actual == expected