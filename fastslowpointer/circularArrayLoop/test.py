import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "input,expected", [
        ([2, -1, 1, 2, 2], True),
        ([-1, -2, -3, -4, -5, 6], False),
        ([1, -1, 5, 1, 4], True),
        ([2, 1, -1, -2], False),
        ([5, 4, -2, -1, 3], False)
    ])
def test(input, expected):
    actual = Solution().circularArrayLoop(input)
    assert actual == expected
