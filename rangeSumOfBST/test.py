import collections

import pytest

from core.exceptions.constraints_violation import ConstraintsViolationException
from .solution import Solution, TreeNode


def from_array(input: list[int]) -> TreeNode:
    if not input:
        raise ConstraintsViolationException()

    q = collections.deque()
    root = None
    for i in range(len(input)):
        curr = TreeNode(input[i]) if input[i] else None
        if i == 0:
            root = curr
        elif i % 2 == 0:
            node = q.popleft()
            node.right = curr
        else:
            node = q[0]
            node.left = curr

        if curr:
            q.append(curr)
    return root


@pytest.mark.parametrize("input, low, high, expected", [
    ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
    ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23)
])
def test(input, low, high, expected):
    root = from_array(input)
    actual = Solution().rangeSumBST(root, low, high)
    assert actual == expected
