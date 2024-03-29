from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        q = deque([root, None])

        while q:
            curr = q.popleft()
            while curr:
                next = q.popleft()
                curr.next = next
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                curr = next
            if q:
                q.append(None)
        return root
