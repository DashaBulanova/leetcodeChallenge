from typing import Optional, List

import pytest

from .solution import Solution, ListNode


def to_array(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def to_linked_list(input) -> Optional[ListNode]:
    if len(input) == 0:
        return None

    curr, hear = None, None
    for i in input:
        if curr is None:
            curr = ListNode(i)
            head = curr
        else:
            curr.next = ListNode(i)
            curr = curr.next
    return head


@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
    ([1, 1, 2, 3, 4], [2, 3, 4]),
    ([1, 1], []),
    ([1, 2, 2], [1])
])
def test(input, expected):
    head = to_linked_list(input)
    actual = Solution().deleteDuplicates(head)
    assert to_array(actual) == expected


"""
1,2,3,3,4,4,5

f=1 s=None
duplicate =()
s=1
f=2
s=1->2
f=3
dupl = {3}
f=3
f=4
dupl={3, 4}
f=4
f=5
s=1-2-5
"""
