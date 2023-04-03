import pytest

from .solution import Solution


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1], [4], [7]], [1, 4, 7]),
    ([[1, 4, 7]], [1, 4, 7]),
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5])
])
def test(matrix, expected):
    actual = Solution().spiralOrder(matrix)
    assert actual == expected
