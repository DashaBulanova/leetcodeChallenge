from typing import List

import pytest

from rotateList.solution import Solution, ListNode


def toLinkedList(input: List) -> ListNode:
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


def toList(head: ListNode) -> List:
    result = []
    node = head
    while node is not None:
        result.append(node.val)
        node = node.next

    return result


@pytest.mark.parametrize("input, k, expected",
                         [
                             ([0, 1, 2], 4, [2, 0, 1]),
                             ([1, 2, 3], 2000000000, [2, 3, 1]),
                         ])
def test_solution(input, k, expected):
    head = toLinkedList(input)
    actual = Solution().rotateRight(head, k)

    assert toList(actual) == expected
