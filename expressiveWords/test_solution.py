import pytest

from .solution import Solution


@pytest.mark.parametrize("s, words, expected", [
    ("heeellooo", ["hello", "hi", "helo"], 1),
    ("helloo", ["hello", "hi", "helo"], 0),
    ("zzzzzyyyyy", ["zzyy", "zy", "zyy"], 3),
    ("dddiiiinnssssssoooo",
     ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"], 3),
    ("aaa", ["aaaa"], 0)
])
def test(s, words, expected):
    actual = Solution().expressiveWords(s, words)
    assert actual == expected


"""
grouping=[(h,1), e:3, l:2, o:3)

group
"""
