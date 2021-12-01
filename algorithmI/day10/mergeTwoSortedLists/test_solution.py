import pytest

from solution import Solution, ListNode


def from_array(input: []) -> [ListNode]:
    head, current = None, None
    for item in input:
        if head is None:
            head = ListNode(item)
            current = head
        else:
            current.next = ListNode(item)
            current = current.next
    return head


def to_array(input: ListNode) -> []:
    result = []
    current = input
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize("input1, input2, expected", [
    ([1, 2, 3], [1, 3, 4], [1, 1, 2, 3, 3, 4])
])
def test(input1, input2, expected):
    list1 = from_array(input1)
    list2 = from_array(input2)
    actual = Solution().mergeTwoLists(list1, list2)
    assert to_array(actual) == expected

# [1,2,4]
# [1,2,3]

# step0:
# pointer = 1
# next=2
# head = 1
# current = 1
# pointer_1=2

# step1:
# pointer_1=2 pointer_2=1
# pointer = pointer_2=1
# next=2
# current = 1->1
# current = 1
# pointer_2=2

# step2:
# pointer_1=2 pointer_2=2
# pointer=pointer_1
# next=4
# head=1->1->2
# current=1->2
# pointer_1 = 4

# step3:
# pointer_1=4 pointer_2=2
# pointer=pointer_2
# next=3
# head=1->1->2->3
# current=2->3
# pointer_1 = None
