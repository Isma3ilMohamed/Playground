class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []  # Renamed from 'increment' to 'inc'

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)  # Initialize increment for this element

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        inc_value = self.inc.pop()
        val = self.stack.pop() + inc_value
        if idx > 0:
            # Propagate the increment to the next element below
            self.inc[idx - 1] += inc_value
        return val

    def increment(self, k: int, val: int) -> None:
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val
