"""
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Input: letters = ["c","f","j"], target = "c"
Output: "f"

Input: letters = ["c","f","j"], target = "d"
Output: "f"

Input: letters = ["c","f","j"], target = "g"
Output: "j"

Input: letters = ["c","f","j"], target = "j"
Output: "c"
"""

"""
Input: letters = ["c","f","j"], target = "d"
Output: "f"
start = 0, end = 2
0 < 2
mid = 1
mid_letter = f
f > target => end = 1
0<1
mid = 0
mid_letter = c
c>d false => go right => start = 1
1<=
"""

"""
["c","f","j"] target = "j", "c"
start = 0, end = 2
mid = 1
mid_letter = f
f<j => start = 2



"""

import pytest

from solution import nextGreatestLetter

@pytest.mark.parametrize("input, target, expected", [
    (["c","f","j"],"d", "f"),
    (["c","f","j"], "g", "j"),
    (["c","f","j"], "a", "c"),
    (["c","f","j"], "c", "f")])
def test(input, target, expected):
    assert nextGreatestLetter(input, target) == expected