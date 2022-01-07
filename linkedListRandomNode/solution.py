
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    __len: int
    __hash: Dict[int, int]

    def __init__(self, head: Optional[ListNode]):
        if head is None:
            raise ValueError('')
        
        self.__hash = {}
        n=0
        node = head
        while node:
            self.__hash[n]=node.val
            node=node.next
            n+=1
        self.__len = n

    def getRandom(self) -> int:
        r = random.randrange(0, self.__len)
        return self.__hash[r]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()