import pytest

from .solution import Solution


@pytest.mark.parametrize("piles, k, expected", [
    ([5, 4, 9], 2, 12),
    ([4, 3, 6, 7], 3, 12)
])
def test(piles, k, expected):
    actual = Solution().minStoneSum(piles, k)
    assert actual == expected
