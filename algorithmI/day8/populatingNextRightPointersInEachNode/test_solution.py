from queue import Queue
from typing import List

import pytest

from core.dataStructure.TreeNode import to_array
from core.utils.treeNodeConvert import to_binary_tree
from .solution import Solution, Node


def to_binary_tree(array: List[int]) -> Node:
    root, curr = None, None
    queue = Queue()

    for item in array:
        if root is None:
            root = Node(item)
            queue.put(root)
        elif curr is None:
            curr = queue.get()
            if item is not None:
                curr.left = Node(item)
                queue.put(curr.left)
        else:
            if item is not None:
                curr.right = Node(item)
                queue.put(curr.right)
            curr = None

    return root


def to_array(root: Node) -> []:
    return breadth_first_traversal(root)


def breadth_first_traversal(root: Node) -> []:
    result = []
    queue = Queue()
    queue.put(root)
    count = 1
    while not queue.empty() and count > 0:
        node = queue.get()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            count -= 1
            if node.left is not None:
                queue.put(node.left)
                count += 1
            else:
                queue.put(None)
            if node.right is not None:
                queue.put(node.right)
                count += 1
            else:
                queue.put(None)
    return result


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 2, 3, 4, 5, 6, 7], [1, None, 2, 3, None, 4, 5, 6, 7, None]),
                         ])
def test_number_of_bits(input, expected):
    root = to_binary_tree(input)
    actual = Solution().connect(root)
    assert to_array(actual) == expected

