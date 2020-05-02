# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self
        current_node = head
        result = ""
        while current_node is not None:
            if result != '':
                result += '->'
            result += str(current_node.val)
            current_node = current_node.next

        result += '->NULL'
        return result


class Solution:
    # idea:
    # 1. Count the length of the linked list
    # 2. Пройти еще раз по linked list и менять на ходу элементы
    def oddEvenList(self, head: ListNode) -> ListNode:
        length = self.get_length(head)

        curr = head
        prev = None

        last_odd = None
        first_even = None

        for i in range(1, length + 1):
            if i % 2 != 0:
                if last_odd is None:
                    last_odd = curr
                else:
                    tail = curr.next
                    last_odd.next = curr
                    prev.next = tail
                    curr.next = first_even

                    last_odd = curr
                    curr = prev
            else:
                if first_even is None:
                    first_even = curr
            prev = curr
            curr = curr.next

        return head

    def get_length(self, head):
        count = 0
        node = head

        while node is not None:
            count += 1
            node = node.next
        return count
