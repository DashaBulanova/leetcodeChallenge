"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from queue import Queue
from typing import List

from core.dataStructure.naryTree import Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_items = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_items.append(node.val)
                if node and node.children:
                    for child in node.children:
                        queue.append(child)

            result.append(level_items)

        return result
