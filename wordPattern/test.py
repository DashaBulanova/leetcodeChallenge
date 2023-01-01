import pytest
from .solution import Solution


@pytest.mark.parametrize("pattern, s, expected", [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
    ("aaa", "aaa aaa aaa aaa", False),
    ("ab", "happy hacking", True),
])
def test(pattern, s, expected):
    actual = Solution().wordPattern(pattern, s)
    assert actual == expected
