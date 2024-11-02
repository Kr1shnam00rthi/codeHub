class MyStack:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        temp=self.queue
        self.queue=[]
        self.queue.append(x)
        for x in temp:
            self.queue.append(x)


    def pop(self) -> int:
        a=self.queue.pop(0)
        return a

    def top(self) -> int:
        return self.queue[0]


    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty() 
