import pytest
from .solution import Solution

@pytest.mark.parametrize("matrix, expected", [
    ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
    ([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
])
def test(matrix, expected):
    actual = Solution().transpose(matrix)
    assert actual == expected

