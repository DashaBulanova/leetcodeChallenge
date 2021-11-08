# Definition for a Node.
from queue import Queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = Queue()
        queue.put((root, 1))

        prev_item = None
        prev_level = 1
        while not queue.empty():
            (item, level) = queue.get()
            if prev_item and prev_level == level:
                prev_item.next = item
            prev_item = item
            prev_level = level
            if item.left:
                queue.put((item.left, level+1))
            if item.right:
                queue.put((item.right, level+1))
        return root
