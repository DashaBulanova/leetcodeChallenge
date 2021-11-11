from .solution import Solution, ListNode


def test():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head.next.next.next.next.next.next = head.next.next
    assert Solution().detectCycle(head) == head.next.next

    head.next.next.next.next.next.next = head.next.next.next
    assert Solution().detectCycle(head) == head.next.next.next

    head.next.next.next.next.next.next = head
    assert Solution().detectCycle(head) == head


