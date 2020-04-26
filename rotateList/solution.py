# Definition for singly-linked list.
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
            result += current_node.val
            current_node = current_node.next

        result += '->NULL'
        return result

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        prev = None
        for i in range(1, k + 1):
            while node.next is not None:
                curr = node
                node = node.next
                prev = curr
            if prev is not None:
                prev.next = None
                node.next = head
                head = node

        return node
