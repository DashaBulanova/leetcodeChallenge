from .solution import has_cycle, Node


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert has_cycle(head) is False

    head.next.next.next.next.next.next = head.next.next
    assert has_cycle(head) is True

    head.next.next.next.next.next.next = head.next.next.next
    assert has_cycle(head) is True
