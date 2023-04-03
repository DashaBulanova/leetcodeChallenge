import pytest

from .solution import Solution


@pytest.mark.parametrize("spells, potions, success, expected", [
    ([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]),
    ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2]),
    ([9, 39], [35, 40, 22, 37, 29, 22], 320, [2, 6])
])
def test(spells: list[int], potions: list[int], success: int, expected: list[int]):
    actual = Solution().successfulPairs(spells, potions, success)
    assert actual == expected
