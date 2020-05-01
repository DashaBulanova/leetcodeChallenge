from typing import List

import pytest

from splitLinkedListInParts.solution import Solution, ListNode


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


def to_flatten_list(list_parts: List[ListNode]):
    result = []
    for item in list_parts:
        result.append(item.to_list() if item is not None else [])

    return result


@pytest.mark.parametrize("input, k, expected",
                         [
                             ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [4, 5], [6, 7]]),
                             ([], 3, [[], [], []]),
                             ([1, 2, 3], 5, [[1], [2], [3], [], []]),
                             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),

                         ])
def test_solution(input, k, expected):
    head = to_linked_list(input)
    actual = Solution().splitListToParts(head, k)

    assert to_flatten_list(actual) == expected
