import pytest
from solution import Node, find_middle_of_linked_list

def test():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  assert 3 == find_middle_of_linked_list(head).value

  head.next.next.next.next.next = Node(6)
  assert 4 == find_middle_of_linked_list(head).value

  head.next.next.next.next.next.next = Node(7)
  assert 4 == find_middle_of_linked_list(head).value
