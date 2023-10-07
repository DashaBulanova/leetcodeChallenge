import pytest

from .solution import Solution, ListNode


def to_linked_list(input):
    head = None
    current = None
    for i in range(len(input)):
        if not head:
            head = ListNode(input[i])
            current = head
        else:
            current.next = ListNode(input[i])
            current = current.next
    return head


@pytest.mark.parametrize("input, expected", [
    ([7, 3, 3, 3, 7], True),
    ([1, 2, 2, 1], True),
    ([1, 2], False),
    ([1, 2, 3, 4, 4, 5, 5, 3, 2, 1], False),
    ([8, 5, 6, 0, 1, 0, 6, 5, 8], True)
])
def test(input, expected):
    head = to_linked_list(input)
    actual = Solution().isPalindrome(head)
    assert actual == expected
