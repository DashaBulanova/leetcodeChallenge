import pytest

from .solution import Solution


@pytest.mark.parametrize("capacity, rocks, additionalRocks, expected", [
    ([2, 3, 4, 5], [1, 2, 4, 4], 2, 3),
    ([10, 2, 2], [2, 2, 0], 100, 3),
    ([10, 2, 2], [2, 2, 0], 5, 2),
    ([10, 2, 2], [10, 2, 2], 5, 3),
])
def test(capacity, rocks, additionalRocks, expected):
    actual = Solution().maximumBags(capacity, rocks, additionalRocks)
    assert actual == expected
