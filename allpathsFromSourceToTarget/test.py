import pytest
from .solution import Solution


@pytest.mark.parametrize("graph, expected", [
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]])
])
def test(graph, expected):
    actual = Solution().allPathsSourceTarget(graph)
    assert actual == expected
