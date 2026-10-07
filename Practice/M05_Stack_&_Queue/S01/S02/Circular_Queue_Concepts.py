class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] *self.size
        self.front = -1
        self.rear = -1
    def enqueue(self, val):
        if self.front == (self.rear + 1) % self.size:
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = val
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        val = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val