from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        stack = deque()

        while True:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break

        while slow:
            stack.append(slow.val)
            slow = slow.next

        slow = head
        while len(stack):
            node = stack.pop()
            if slow.val == node:
                slow = slow.next
            else:
                return False

        return True


"""
7, 3, 3, 3, 3 7
         |
              |
"""
