import pytest

from .solution import Solution


@pytest.mark.parametrize("arr, k, expected", [
    ([2, 3, 4, 7, 11], 5, 9),
    ([1, 2, 3, 4], 2, 6)
])
def test(arr, k, expected):
    actual = Solution().findKthPositive(arr, k)
    assert actual == expected
