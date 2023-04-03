import pytest
from .solution import Solution

@pytest.mark.parametrize("people, limit, expected", [
    ([1,2], 3, 1),
    ([3,2,2,1], 3, 3),
    ([3,5,3,4], 5, 4)
])
def test(people, limit, expected):
    actual = Solution().numRescueBoats(people, limit)
    assert actual == expected

