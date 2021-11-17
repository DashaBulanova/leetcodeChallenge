class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(start_node):
    prev = None
    current = start_node
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def is_palindromic_linked_list(head):
    if not head and not head.next:
        return True

    result = True
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    middle_pointer = slow
    most_right = reverse(middle_pointer)

    right = most_right
    left = head
    while left != right and left and right:
        if left.value != right.value:
            result = False
            break
        left = left.next
        right = right.next

    reverse(most_right)
    return result
