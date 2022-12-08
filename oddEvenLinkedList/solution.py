# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        result = curr
        last_odd = None
        index = 1
        while curr:
            if index % 2 == 0:
                p = curr
                n=curr.next
                p.next = curr.next.next
                n.next=p

                curr.next.next = None
            else:
                c = last_odd.next
                c.next = None
                prev_odd.next = curr
                curr.next = c
                prev_odd = curr
            curr = curr.next
            index += 1
        return result


"""
   |
1->2->3->4->5
1->2
n=3->4->5
p=2
p=2-4-5
n=3-2-4-5
1->3->2->4->5
#1->2->3->4->5
curr = 1->2->3->4->5
prev_od = None

prev_od = 1->2->3->4->5
curr=2->3->4->5

p=1->2->3->4->5
c=2
p=1

"""
