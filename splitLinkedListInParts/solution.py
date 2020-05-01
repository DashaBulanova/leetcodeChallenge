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
    # idea:
    # 1. Count the length of the linked list
    # 2. Determine the length of nodes in each chunk
    # 3. Splitting the linked list up
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if k == 0:
            return []

        length = self.get_length(root)

        quotation = length // k
        reminder = length % k

        groups = [quotation + 1] * reminder + [quotation]*(k-reminder)
        result = [] * k
        currentNode = root

        for i, item_count in enumerate(groups):

            result.append(currentNode)

            for j in range(item_count-1):
                currentNode = currentNode.next

            if currentNode:
                next = currentNode.next
                currentNode.next = None
            else:
                next = None

            currentNode = next

        return result

    def get_length(self, head):
        count = 0
        node = head

        while node is not None:
            count += 1
            node = node.next
        return count
