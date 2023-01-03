
import collections


class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
        self.score = 0


def from_array(nodes: list[int]) -> "TreeNode":
    root = TreeNode(nodes[0])
    q = collections.deque()
    q.append(root)
    for i in range(1, len(nodes)):
        if nodes[i] == q[0]:
            if q[0].left is None:
                q[0].left = TreeNode(i)
                q.append(q[0].left)
            else:
                c = q.pop()
                c.right = TreeNode(i)
                q.append(c.right)
        else:
            q.pop()

    return root


def calculate_score(node) -> int:
    if node is None:
        return 0

    left_score, right_score = 0, 0
    if node.left is not None:
        right_score = calculate_score(node.left)
    if node.right is not None:
        left_score = calculate_score(node.right)

    node.score = left_score+right_score+1
    return node.score


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        root = from_array(sorted(parents))
        calculate_score(root)
