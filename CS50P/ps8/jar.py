class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a non-negative int")

        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("There is not enough cookies")
        elif size > self.capacity:
            raise ValueError("There is not enough space")

        self._size = size