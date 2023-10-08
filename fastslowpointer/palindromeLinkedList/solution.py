from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head) -> ListNode:
    if not head or not head.next:
        return head

    prev = None
    current = head

    next = current.next
    while current:
        current.next = prev
        prev = current
        current = next
        if current:
            next = current.next

    return prev


""""
     None <- 0 <-6<-5 <- 8   None
prev                     |
cur                            |
next                           | 

current = 0 -> 6 -> 5 -> 8
x = 5 -> 8
c = 6 -> 5 -> 8
c = 6

0 -> 6 -> 0 -> 6 -> 5 -> 8
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while True:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
        reversed = reverse(slow)

        slow = head
        while reversed:
            if slow.val == reversed.val:
                slow = slow.next
                reversed = reversed.next
            else:
                return False

        return True


"""
7, 3, 3, 3, 3 7
         |
              |
"""
