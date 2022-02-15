from collections import deque

import pytest

from .solution import Solution, Node


def to_tree(input) -> Node:
    if len(input)==0:
        return None
    root = Node(input[0])
    q = deque([root])
    for i in range(1, len(input), 2):
        node = q.popleft()
        if input[i]:
            node.left = Node(input[i])
            q.append(node.left)
        if input[i + 1]:
            node.right = Node(input[i + 1])
            q.append(node.right)
    return root


@pytest.mark.parametrize("input", [
    ([1, 2, 3, 4, 5, None, 7]),
    ([])
])
def test(input):
    root = to_tree(input)
    root = Solution().connect(root)

    assert root.val == 1
    assert root.next is None
    assert root.left.next.val == 3
    assert root.right.next is None
    assert root.left.left.next.val == 5
    assert root.left.right.next.val == 7
    assert root.right.right.next is None
