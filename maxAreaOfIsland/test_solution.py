import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
     ([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
    ([[0,0,0,0,0,0,0,0]], 0),
    ([[1]], 1)
    #[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
])
def test(input, expected):
    actual = Solution().maxAreaOfIsland(input)
    assert actual == expected
