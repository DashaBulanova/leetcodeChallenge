import pytest
from .solution import Solution, TreeNode
from collections import deque


def _convert_to_node(input) -> TreeNode:
    root = TreeNode(input[0])
    q = deque()
    q.append(root)
    i = 1
    while q and i < len(input):
        node = q.popleft()

        if input[i]:
            l = TreeNode(input[i])
            node.left = l
            q.append(l)
        if i + 1 < len(input) and input[i + 1]:
            r = TreeNode(input[i + 1])
            node.right = r
            q.append(r)

        i += 2
    return root


@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3, 4], "1(2(4))(3)"),
    ([1,2,3,None,4], "1(2()(4))(3)")
])
def test(input, expected):
    root = _convert_to_node(input)
    actual = Solution().tree2str(root)
    assert actual == expected
