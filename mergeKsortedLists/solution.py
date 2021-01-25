# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List
from heapq import heapify, heappush, heappop



class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        heapify(heap)

        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        for item in lists:
            if item:
                heappush(heap, item)

        head = None
        current = None
        while heap:
            min_value = heappop(heap)
            min_item = ListNode(min_value.val)

            if head is None:
                head = min_item
                current = head
            else:
                current.next = min_item
                current = min_item

            next_item = min_value.next
            if next_item:
                heappush(heap, next_item)

        return head