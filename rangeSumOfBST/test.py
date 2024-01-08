import pytest
from collections import deque
from .solution import Solution, TreeNode


def _to_tree(input: list[int | None]) -> TreeNode:
    if not input or input[0] is None:
        raise ValueError()

    root = TreeNode(input[0])
    q = deque([root])

    for i in range(1, len(input)):
        new = TreeNode(input[i])
        if input[i] is not None:
            if i % 2 == 0:
                q[0].right = new
            else:
                q[0].left = new
        if input[i] is not None:
            q.append(new)
        if i % 2 == 0:
            q.popleft()

    return root


@pytest.mark.parametrize("input, low, high, expected", [
    ([10,5,15,3,7,None,18],7, 15, 32),
    ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23)
])
def test(input, low, high, expected):
    root = _to_tree(input)
    actual = Solution().rangeSumBST(root, low, high)
    assert actual == expected
