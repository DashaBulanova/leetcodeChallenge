import pytest
from .solution import Solution

@pytest.mark.parametrize("s1, s2, expected", [
("ab", "eidbaooo", True),
("ab", "eidboaoo", False),
("adc", "dcda", True)
])
def test(s1, s2, expected):
    actual = Solution().checkInclusion(s1, s2)
    assert actual == expected
"""
 s1 = "adc", s2 = "dcda"

hash = {a:1, b:1, c:1}
need=3

start =0 e=0
s2[0]=e in hash False=>
    0=0
    start=1
e=1
s2[1]=i in hash False => 1<=1: start=2
e=2
s2[1]=d in hash False => 2<=2 start=3
e=3
s2[1]=b in hash True =>
    hash = {a:1, b:0}
    need = 1
e=4
s2[4]=a in hash True
"""