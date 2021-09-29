class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, val: int) -> None:
        self.queue.append(val)

    def pop(self) -> None:
        self.queue.pop(0)

    def show(self) -> list:
        return self.queue


my = Queue()
my.push(1)
my.push(2)
my.push(3)
print(my.show())
my.pop()
print(my.show())



