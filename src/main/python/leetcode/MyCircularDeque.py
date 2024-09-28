class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = [0] * k
        self.front = k - 1  # Initialize front pointer
        self.rear = 0       # Initialize rear pointer
        self.count = 0      # Number of elements

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.front] = value
        self.front = (self.front - 1) % self.capacity
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.front + 1) % self.capacity
        return self.deque[index]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.rear - 1) % self.capacity
        return self.deque[index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
