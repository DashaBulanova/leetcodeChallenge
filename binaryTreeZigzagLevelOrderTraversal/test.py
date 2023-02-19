import collections

import pytest

from .solution import TreeNode, Solution


def __from_array(input: list[int | None]) -> TreeNode | None:
    if not input:
        return None

    root = TreeNode(input[0])
    q = collections.deque([root])
    for i in range(1, len(input), 2):
        curr = q.popleft()
        if input[i] is not None:
            curr.left = TreeNode(input[i])
            q.append(curr.left)
        if input[i + 1] is not None:
            curr.right = TreeNode(input[i + 1])
            q.append(curr.right)
    return root


@pytest.mark.parametrize("input, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
    ([1], [[1]]),
    ([], []),
    ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]])
])
def test(input, expected):
    root = __from_array(input)
    actual = Solution().zigzagLevelOrder(root)
    assert actual == expected
