from collections import deque
from typing import List

import pytest

from .solution import Solution, TreeNode


def to_tree(input: List[int]) -> TreeNode:
    if len(input) == 0:
        return None

    q = deque()
    root = TreeNode(input[0])
    q.append(root)

    for i in range(1, len(input), 2):
        node = q.popleft()
        if input[i] is not None:
            node.left = TreeNode(input[i])
            q.append(node.left)
        if input[i + 1] is not None:
            node.right = TreeNode(input[i + 1])
            q.append(node.right)

    return root


@pytest.mark.parametrize("input, expected", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2)
])
def test(input, expected):
    root = to_tree(input)
    actual = Solution().maxDepth(root)
    assert actual == expected
