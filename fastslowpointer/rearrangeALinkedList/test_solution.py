from solution import reorder, Node


def test():
    # 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    root = Node(2)
    root.next = Node(4)
    root.next.next = Node(6)
    root.next.next.next = Node(8)
    root.next.next.next.next = Node(10)
    root.next.next.next.next.next = Node(12)
    actual = reorder(root)

    assert actual.to_list() == [2, 12, 4, 10, 6, 8]
