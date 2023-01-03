import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([3, 1, 2, 4], 17),
    ([11, 81, 94, 43, 3], 444)
])
def test(input, expected):
    actual = Solution().sumSubarrayMins(input)
    assert actual == expected
