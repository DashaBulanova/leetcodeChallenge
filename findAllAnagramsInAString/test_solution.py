import pytest

from .solution import Solution


@pytest.mark.parametrize("s,p, expected", [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2])
])
def test(s, p, expected):
    actual = Solution().findAnagrams(s, p)
    assert actual == expected


"""
s=cbaebabacd 
p=abc

result = []
expected = {'a':1, b:1, c:1}

start =0 

end=0
actual={c:1}
0-0+1=1 len(p)==3

end=1
actual={c:1, b:1}
2!=3

end=2
actual={c:1, b:1, a:1}
3=3 => result=[0]
    actual={b:1, a:1}
    start = 1

end=3
actual={b:1, a:1, e:1}
3=3 
"""
