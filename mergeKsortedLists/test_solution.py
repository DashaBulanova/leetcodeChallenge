import pytest

from mergeKsortedLists.solution import Solution, ListNode


def test_number_of_bits():
    input = [ListNode(1,ListNode(4, ListNode(5))),
             ListNode(1, ListNode(3, ListNode(4))),
             ListNode(2, ListNode(6))]
    actual = Solution().mergeKLists(input)

    assert actual is not None
