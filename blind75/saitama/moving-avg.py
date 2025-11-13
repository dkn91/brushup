from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        # Add new value
        self.queue.append(val)
        self.sum += val
        
        # Remove oldest value if window is full
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        
        # Compute average
        return self.sum / len(self.queue)


[[3], [1], [10], [3], [5]]

