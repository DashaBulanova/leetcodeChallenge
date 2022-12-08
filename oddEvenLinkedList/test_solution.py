import pytest

from .solution import Solution, ListNode

def test():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    actual = Solution().oddEvenList(head)
    assert actual.val == 1
    assert actual.next.val == 3
    assert actual.next.next.val == 5
    assert actual.next.next.next.val == 2
    assert actual.next.next.next.next.val == 4
