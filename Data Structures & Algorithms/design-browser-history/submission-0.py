class ListNode:
    def __init__(self, val, back=None, forward=None):
        self.val = val
        self.back = back
        self.forward = forward
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage= ListNode(homepage)
        self.point = self.homepage

    def visit(self, url: str) -> None:
        page = ListNode(url,back=self.point)
        self.point.forward = page
        self.point = self.point.forward
        

    def back(self, steps: int) -> str:
        while self.point.back and steps > 0:
            self.point = self.point.back
            steps-=1
        return self.point.val
        

    def forward(self, steps: int) -> str:
        count = 0
        while self.point.forward and count != steps:
            self.point = self.point.forward
            count+=1
        return self.point.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)