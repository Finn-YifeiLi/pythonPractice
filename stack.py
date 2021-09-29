class stack:
    def __init__(self) -> None:
        self.myStack = []

    def pop(self) -> None:
        self.myStack.pop()
    
    def push(self, val: int):
        self.myStack.append(val)

    def peek(self):
        print("Top of Stack:", self.myStack[-1])


stack1 = stack()
stack1.push(1)
stack1.peek()
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.pop()
stack1.peek()