class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head: Node):
    setattr(Node, "parent", lambda self, other: self.val <= other.val)

    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next:
        slow_prev = slow_pointer
        slow_pointer = slow_pointer.next
        fast_prev = fast_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer and slow_prev != fast_prev:
            return slow_pointer

    return head
