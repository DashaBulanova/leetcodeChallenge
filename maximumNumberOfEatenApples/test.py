import pytest
from .solution import Solution


@pytest.mark.parametrize("input, days, expected", [
    ([1, 2, 3, 5, 2], [3, 2, 1, 4, 2], 7),
    ([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2], 5)
])
def test(input, days, expected):
    actual = Solution().eatenApples(input, days)
    assert actual == expected
