import pytest
from collections import deque
from .solution import Solution, TreeNode

def _to_tree(input)->TreeNode:
    root = None
    q = deque()
    for i in range(len(input)):
        if i == 0:
            root = TreeNode(input[i])
            q.append(root)
        elif i%2 == 0:
            node = q.popleft()
            if input[i] is None:
                continue
            node.right = TreeNode(input[i])
            q.append(node.right)
        else:
            node = q[0]
            if input[i] is None:
                continue
            node.left = TreeNode(input[i])
            q.append(node.left)

    return root

@pytest.mark.parametrize("input1, input2, expected", [
    ([1,2,3],[1,3,2], False),
    ([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8], True)
])
def test(input1, input2, expected):
    root1 = _to_tree(input1)
    root2 = _to_tree(input2)
    actual = Solution().leafSimilar(root1, root2)
    assert actual == expected

