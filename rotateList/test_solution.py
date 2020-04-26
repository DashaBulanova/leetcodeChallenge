import pytest

from rotateList.solution import Solution, ListNode


def toLinkedList(input: str) -> ListNode:
    head = None
    current_node = head

    for c in input.split('->'):
        if head is None:
            head = ListNode(c)
            current_node = head
        elif c == 'NULL':
            current_node.next = None
            current_node = current_node.next
        else:
            current_node.next = ListNode(c)
            current_node = current_node.next

    return head


@pytest.mark.parametrize("input, k, expected",
                         [
                             ("1->2->3->4->5->NULL", 2, "4->5->1->2->3->NULL"),
                         ])
def test_solution(input, k, expected):
    head = toLinkedList(input)
    actual = Solution().rotateRight(head, k)
    assert str(actual) == expected
