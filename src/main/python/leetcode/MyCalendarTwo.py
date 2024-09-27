class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Step 1: Check for triple booking
        for s, e in self.overlaps:
            if start < e and s < end:
                return False

        # Step 2: Update overlaps
        for s, e in self.bookings:
            if start < e and s < end:
                # There is an overlap between [start, end) and [s, e)
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.overlaps.append((overlap_start, overlap_end))

        # Step 3: Add the new booking
        self.bookings.append((start, end))
        return True
