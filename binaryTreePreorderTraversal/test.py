import pytest

from .solution import Solution, from_array


@pytest.mark.parametrize("tree, expected", [
    ([1, None, 2, 3], [1, 2, 3]),
    ([], []),
    ([1], [1])
])
def test(tree, expected):
    root = from_array(tree)
    actual = Solution().preorderTraversal(root)
    assert actual == expected
