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

        for i in range(0, k):

            item_count = max(1, quotation + min(1, reminder))
            reminder -= min(1, reminder)

            j = 1
            result.append(currentNode)
            while j != item_count:
                j += 1
                currentNode = currentNode.next

            if currentNode is None:
                next = None
            else:
                next = currentNode.next
                currentNode.next = None
            currentNode = next

        return result

    def get_length(self, head):
        count = 0
        node = head

        while node is not None:
            count += 1
            node = node.next
        return count
