import pytest
from solution import Solution


@pytest.mark.parametrize("n, expected", [(3, 3), (1, 0), (51, 20), (100, 14), (27, 9)])
def test(n, expected):
    actual = Solution().minSteps(n)
    assert actual == expected


"""
A
res = 3, op=0
primes=[1,2] 1, -1, -1
    i=1 

"""
