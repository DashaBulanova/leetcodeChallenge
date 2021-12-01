# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        pointer_1 = list1
        pointer_2 = list2
        current = None
        head = None

        while pointer_1 or pointer_2:
            if pointer_1 is not None and pointer_2 is not None:
                if pointer_1.val < pointer_2.val:
                    pointer = pointer_1
                else:
                    pointer = pointer_2
            elif pointer_1 is None:
                pointer = pointer_2
            else:
                pointer = pointer_1

            next = pointer.next
            if current is None:
                head = pointer
                current = pointer
            else:
                current.next = pointer
                current = current.next
            if pointer_1 is not None and pointer_2 is not None:
                if pointer_1.val < pointer_2.val:
                    pointer_1 = next
                else:
                    pointer_2 = next
            elif pointer_1 is not None:
                pointer_1 = next
            else:
                pointer_2 = next

        return head
