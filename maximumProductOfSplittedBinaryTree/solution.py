import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_array(input):
    root = None
    q = collections.deque()
    for i in range(len(input)):
        current = None
        if input[i] is not None:
            current = TreeNode(input[i])
            q.append(current)

        if i == 0:
            root = current
        elif i % 2 == 0:
            node = q.popleft()
            node.right = current
        else:
            node = q[0]
            node.left = current

    return root


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.__calculate_total_sum(root)
        return self.__max_product(root, total_sum)[1]
        #answer should be returned as modulo max%(10**9+7)

    def __calculate_total_sum(self, node):
        if node is None:
            return 0
        left_sum = self.__calculate_total_sum(node.left)
        right_sum = self.__calculate_total_sum(node.right)
        return left_sum + right_sum + node.val

    def __max_product(self, node, total_sum) -> (int, int):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return node.val, (total_sum - node.val) * node.val
        left = self.__max_product(node.left, total_sum)
        right = self.__max_product(node.right, total_sum)
        sum = node.val + left[0] + right[0]
        head = (total_sum - sum)*sum
        return sum, max(head, left[1], right[1])

