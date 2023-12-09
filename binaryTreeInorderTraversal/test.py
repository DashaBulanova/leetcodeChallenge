from collections import deque
import pytest

from .solution import Solution, TreeNode


def _convert(input: list[int]) -> TreeNode:
    root = TreeNode(input[0])
    q = deque([root])
    for i in range(1, len(input), 2):
        node = q.popleft()
        if input[i]:
            node.left = TreeNode(input[i])
            q.append(node.left)
        if i+1 < len(input) and input[i+1]:
            node.right = TreeNode(input[i+1])
            q.append(node.right)

    return root

@pytest.mark.parametrize("input, expected", [
    ([1,None,2,3],[1,3,2])
])
def test(input, expected):
    root = _convert(input)
    actual = Solution().inorderTraversal(root)
    assert actual == expected
