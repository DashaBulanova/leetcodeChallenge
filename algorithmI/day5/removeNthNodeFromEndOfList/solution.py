# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_pointer = None
        fast_poiner = head

        count = 1
        while fast_poiner is not None:
            if count != n+1:
                fast_poiner = fast_poiner.next
                count += 1
            else:
                if slow_pointer is None:
                    slow_pointer = head
                else:
                    slow_pointer = slow_pointer.next
                fast_poiner = fast_poiner.next

        if slow_pointer is None:
            return head.next
        else:
            if slow_pointer.next is not None:
                slow_pointer.next = slow_pointer.next.next
                return head

        return []
