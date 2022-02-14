from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f, s = head, None
        head = None
        duplicate = set()
        while f:
            if f.val not in duplicate:
                if f.next and f.val == f.next.val:
                    duplicate.add(f.val)
                else:
                    if s:
                        s.next = f
                        s = s.next
                    else:
                        s = f
                        head = s
            f = f.next
        if s:
            s.next = None
        return head
