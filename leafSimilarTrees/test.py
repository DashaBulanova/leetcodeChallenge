import pytest

from .solution import Solution, from_array


@pytest.mark.parametrize("tree, expected", [
    # ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 7),
    # ([1, None, 2, None, 0, 3], 3),
    ([8, None, 1, 5, 6, 2, 4, 0, None, 7, 3], 8)
])
def test(tree, expected):
    root = from_array(tree)
    actual = Solution().maxAncestorDiff(root)
    assert actual == expected
