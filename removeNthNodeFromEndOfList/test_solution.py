from typing import List

import pytest

from .solution import Solution, ListNode


def to_linked_list(input: List[int]) -> ListNode:
    head = None
    curr = None
    for i in input:
        if not head:
            head = ListNode(i)
            curr = head
        else:
            curr.next = ListNode(i)
            curr = curr.next

    return head


def to_array(head: ListNode) -> List[int]:
    curr = head
    result = []
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


@pytest.mark.parametrize("input,n, expected", [
     ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
     ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
     ([1], 1, []),
     ([1, 2], 1, [1])
])
def test(input, n, expected):
    head = to_linked_list(input)
    actual = Solution().removeNthFromEnd(head, n)
    arr = to_array(actual)
    assert arr == expected


"""
  1->2->3->4->5
i 0
f    |
s

    1->2
i=2
f      |
s|
"""
