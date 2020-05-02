from typing import List

import pytest

from oddEvenLinkedList.solution import Solution, ListNode


def to_linked_list(input: List) -> ListNode:
    head = None
    current_node = None

    for i in input:
        if head is None:
            head = ListNode(i)
            current_node = head
        else:
            current_node.next = ListNode(i)
            current_node = current_node.next

    return head


def to_list(head: ListNode):
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    return result


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
                             ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),

                         ])
def test_solution(input, expected):
    head = to_linked_list(input)
    i = str(head)
    actual = Solution().oddEvenList(head)

    assert to_list(actual) == expected
