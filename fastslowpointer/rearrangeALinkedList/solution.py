from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def to_list(self):
        result = list()
        current = self
        while current:
            result.append(current.value)
            current = current.next
        return result

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reverse(node):
    prev = None
    current = node
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reorder(head):
    # TODO: Write your code here
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow
    most_right = reverse(middle)

    current = head
    change_for = most_right
    while current:
        next = current.next
        current.next = change_for
        current = current.next
        change_for = next

    return head


"""
2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
1. define middle pointer use slow and fast strategy
middle point will be 8
2. reverse second half
2 -> 4 -> 6->8<-10<-12, 8->none
3. go from left and right 
4. swap the next pointers at left elements
2->12->10 4->10->6->8->None
left=left.next
right=right.next
2.next

"""
