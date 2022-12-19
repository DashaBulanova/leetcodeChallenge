import pytest

from .solution import Solution


@pytest.mark.parametrize("n, edges, source, destination, expected", [
    (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
    (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    (6, [[0, 1], [0, 2], [2, 4], [5, 4], [4, 3]], 0, 5, True),
    (10, [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [
     4, 2], [7, 4], [4, 0], [0, 9], [5, 4]], 5, 9, True)
])
def test(n, edges, source, destination, expected):
    actual = Solution().validPath(n, edges, source, destination)
    assert actual == expected
