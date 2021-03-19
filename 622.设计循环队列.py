class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = k * [None]
        self.head = 0
        self.tail = 0
        self.size = k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail-1]


    def isEmpty(self) -> bool:
        if self.head == self.tail and self.queue[self.head] == None:
            return True
        return False


    def isFull(self) -> bool:
        if self.head == self.tail and self.queue[self.head] != None:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()