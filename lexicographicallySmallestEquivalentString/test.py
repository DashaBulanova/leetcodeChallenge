import pytest

from .solution import Solution


@pytest.mark.parametrize("s1,s2,baseStr, expected", [
    ("parker", "morris", "parser", "makkek"),
    ("hello", "world", "hold", "hdld"),
   ("leetcode", "programs", "sourcecode", "aauaaaaada"),
   ("aabbbabbbbbabbbbaabaabbaaabbbabaababaaaabbbbbabbaa", "aabbaabbbabaababaabaababbbababbbaaaabbbbbabbbaabaa", "buqpqxmnajphtisernebttymtrydomxnwonfhfjlzzrfhosjct","auqpqxmnajphtiserneattymtrydomxnwonfhfjlzzrfhosjct")
])
def test(s1, s2, baseStr, expected):
    actual = Solution().smallestEquivalentString(s1, s2, baseStr)
    assert actual == expected
