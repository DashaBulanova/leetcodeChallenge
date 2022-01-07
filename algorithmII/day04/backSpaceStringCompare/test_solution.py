import pytest

from .solution import Solution


@pytest.mark.parametrize("str1, str2, expected", [
    # ("ab#c", "ad#c", True),
    # ("ab##", "c#d#", True),
    # ("a#c", "b", False),
    # ("y#fo##f", "y#f#o##f", True),
    ("nzp#o#g", "b#nzp#o#g", True)
])
def test(str1, str2, expected):
    actual = Solution().backspaceCompare(str1, str2)
    assert actual == expected


"""
str1="y#fo## f", str2 = "y#f#o## f"
p1=6 p2=7

p1=5 p2=6

count1=2
p1=3
count1=1
p1=2
count=0
p1=1
count=1
p1=0
count1=0
p1=-1

y#f#o##
p2=6
count





"""
