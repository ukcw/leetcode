class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.capacity = k  # 1-index
        self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[(self.front + self.size) % self.capacity] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + self.size) % self.capacity - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
