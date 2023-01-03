import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([-1, 2, 0, 2, 0], 3)
])
def test(input, expected):
    actual = Solution().countHighestScoreNodes(input)
    assert actual == expected
