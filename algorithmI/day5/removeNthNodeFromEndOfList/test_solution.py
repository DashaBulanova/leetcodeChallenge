import pytest

from .solution import Solution, ListNode


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
                             ([1, 2], 2, [2]),
                             ([1], 1, []),
                         ])
def test_number_of_bits(input, target, expected):
    head = None
    cur_node = None
    for i in input:
        if not head:
            head = ListNode(i)
            cur_node = head
        else:
            node = ListNode(i)
            cur_node.next = node
            cur_node = node
    actual = Solution().removeNthFromEnd(head, target)

    result = []
    node = actual
    while node:
        result.append(node.val)
        node = node.next
    assert result == expected
