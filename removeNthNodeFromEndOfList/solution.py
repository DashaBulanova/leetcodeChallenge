from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        f, s, n = head, None, None

        i = 1
        while f is not None:
            f = f.next

            if i >= k-1:
                if k - 1 == 0:
                    n = f
                else:
                    n = head if n is None else n.next
            if i >= k+1:
                s = head if s is None else s.next
            i += 1

        if s is None:
            return n if n is not None else None

        s.next = n
        return head
