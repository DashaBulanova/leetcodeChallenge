import pytest
from .solution import Solution

@pytest.mark.parametrize("input, k, expected", [
([1,1,1], 2, 2),
([1,2,3], 3, 2),
([1,-1,0], 0, 3)
])
def test(input, k, expected):
    actual = Solution().subarraySum(input, k)
    assert actual == expected

"""
[1,-1,0] k=0
s, e=0,0, acc = 0, res = 0

e=0
acc = 1 False
e=1
acc=3 => res=1 acc=2 start=1
e=2
acc=5

1<=2
acc=3 start=2
res=2 start=3
"""