import pytest

from .solution import Solution


@pytest.mark.parametrize("tasks, expected", [
    ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
    ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
    ([[46, 9], [46, 42], [30, 46], [30, 13], [30, 24], [30, 5], [30, 21], [29, 46], [29, 41], [29, 18], [29, 16],
      [29, 17], [29, 5], [22, 15], [22, 13], [22, 25], [22, 49], [22, 44]],
     [14, 5, 12, 3, 0, 13, 10, 11, 9, 6, 4, 15, 8, 1, 17, 2, 7, 16])
])
def test(tasks, expected):
    actual = Solution().getOrder(tasks)
    assert actual == expected
