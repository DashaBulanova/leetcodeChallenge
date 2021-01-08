from queue import Queue
from typing import List

from core.dataStructure.TreeNode import TreeNode


def to_binary_tree(array: List[int]) -> TreeNode:

    root, curr = None, None
    queue = Queue()

    for item in array:
        if root is None:
            root = TreeNode(item)
            queue.put(root)
        elif curr is None:
            curr = queue.get()
            if item is not None:
                curr._left = TreeNode(item)
                queue.put(curr._left)
        else:
            if item is not None:
                curr.right = TreeNode(item)
                queue.put(curr.right)
            curr = None

    return root
