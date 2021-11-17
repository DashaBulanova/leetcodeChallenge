class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(start_node, end_node):
    if start_node == end_node:
        return

    prev = None
    current = start_node
    while prev != end_node:
        next = current.next
        current.next = prev
        prev = current
        current = next


def is_palindromic_linked_list(head):
    if not head:
        return False
    if not head.next:
        return True
    slow_pointer = head
    fast_pointer = head

    most_right = head
    while fast_pointer and fast_pointer.next:
        most_right = fast_pointer.next
        fast_pointer = fast_pointer.next.next
        if fast_pointer:
            most_right = fast_pointer
        slow_pointer = slow_pointer.next

    middle_pointer = slow_pointer
    reverse(middle_pointer, most_right)

    right_pointer = most_right
    left_pointer = head
    while left_pointer != right_pointer and left_pointer and right_pointer:
        if left_pointer.value != right_pointer.value:
            return False
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    reverse(most_right, middle_pointer)
    return True
