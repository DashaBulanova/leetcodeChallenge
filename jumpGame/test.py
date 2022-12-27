import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([2, 0], True)
])
def test(input, expected):
    actual = Solution().canJump(input)
    assert actual == expected
