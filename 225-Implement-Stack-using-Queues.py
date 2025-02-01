class MyStack:

    def __init__(self):
        self.queue1 = []
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

        

    def pop(self) -> int:
        v = self.queue1[-1]
        self.queue1.pop()
        return v
        

    def top(self) -> int:
        return self.queue1[-1]
        

    def empty(self) -> bool:
        if (self.queue1 == []) :
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()