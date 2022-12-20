import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([[1, 3], [3, 0, 1], [2], [0]], False),
    ([[1], [2], [3], []], True)
])
def test(input, expected):
    actual = Solution().canVisitAllRooms(input)
    assert actual == expected
