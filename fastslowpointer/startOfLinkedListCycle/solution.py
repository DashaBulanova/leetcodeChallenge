class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow_pointer = head
        fast_pointer = head
        has_cycle = False

        # define is cycle exist
        while fast_pointer and fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # define lenght of the cycle
        lenght = 0
        lenght_defined = False
        while not lenght_defined:
            fast_pointer = fast_pointer.next
            lenght += 1
            if fast_pointer == slow_pointer:
                lenght_defined = True

        # define start point
        start_pointer = head
        fast_pointer = head
        i = 0

        start_defined = False
        while not start_defined:
            fast_pointer = fast_pointer.next
            i += 1
            if i > lenght:
                start_pointer = start_pointer.next
            if fast_pointer == start_pointer:
                break

        return start_pointer
#time complexity O(3N)
#space complexity: O(1)