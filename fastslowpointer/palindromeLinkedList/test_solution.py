from solution import Node, is_palindromic_linked_list


def test():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    assert is_palindromic_linked_list(head)

    head.next.next.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is False


def test_1():
    head = Node(1)
    head.next = Node(2)
    # head.next.next = Node(2)
    # head.next.next.next = Node(1)

    assert is_palindromic_linked_list(head) is False
