import collections

class ListNode:
    def __init__(self, value, prev: "ListNode" = None, next: "ListNode" = None):
        self.value = value
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)
        self.current = self.root

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.current.next = node
        prev = self.current
        self.current = node
        self.current.prev = prev

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev

        return self.current.value

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next

        return self.current.value

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)