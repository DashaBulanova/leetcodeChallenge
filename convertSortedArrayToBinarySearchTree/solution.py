# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from core.dataStructure import TreeNode
from core.dataStructure.src.ListNode import ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        current = head
        while current.next is not None:

