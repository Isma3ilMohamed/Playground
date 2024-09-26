import bisect

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.starts, start)
        # Check for overlap with previous event
        if idx > 0 and start < self.ends[idx - 1]:
            return False
        # Check for overlap with next event
        if idx < len(self.starts) and end > self.starts[idx]:
            return False
        # No overlap; insert the event
        self.starts.insert(idx, start)
        self.ends.insert(idx, end)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
