import pytest
from .solution import Solution, TreeNode


@pytest.mark.parametrize("p_arr, q_arr, expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False)
])
def test(p_arr, q_arr, expected):
    p = TreeNode.create(p_arr)
    q = TreeNode.create(q_arr)

    actual = Solution().isSameTree(p, q)
    assert actual == expected
