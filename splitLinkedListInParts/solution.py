# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        current_node = self
        result = []
        while current_node is not None:
            result.append(current_node.val)
            current_node = current_node.next
        return result


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if k == 0:
            return []

        length = self.get_length(root)

        quotation = length // k
        reminder = length % k

        result = [] * k
        currentNode = root
        if quotation > 0:
            for i in range(0, k):

                if reminder == 0:
                    item_count = quotation
                else:
                    item_count = quotation + 1
                    reminder -= 1

                j = 1
                result.append(currentNode)
                while j != item_count:
                    j += 1
                    currentNode = currentNode.next

                next = currentNode.next
                currentNode.next = None
                currentNode = next
        else:
            for i in range(0, reminder):
                result.append(currentNode)
                next = currentNode.next
                currentNode.next = None
                currentNode = next

            for i in range(0, k-reminder):
                result.append(None)

        return result

    def get_length(self, head):
        count = 0
        node = head

        while node is not None:
            count += 1
            node = node.next
        return count
