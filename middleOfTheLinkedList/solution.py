class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        mid = head
        len=0
        while curr:
            len+=1
            curr=curr.next
        
        i=0
        if len%2 == 0:
            mid_index=len/2
        else:
            mid_index=len/2 - 1
        while i < mid_index:
            i+=1
            mid=mid.next

        return mid
