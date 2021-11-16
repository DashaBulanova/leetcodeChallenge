class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  fast_pointer = head
  slow_pointer = head

  while fast_pointer and fast_pointer.next:
  	fast_pointer = fast_pointer.next.next
  	slow_pointer = slow_pointer.next
  
  return slow_pointer