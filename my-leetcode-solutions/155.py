class MinStack:

    def __init__(self):
        self.elements=[]

    def push(self, val: int) -> None:
        self.elements.append(val)

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return min(self.elements)




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
