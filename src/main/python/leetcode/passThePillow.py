class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # The cycle length is 2 * (n - 1)
        cycle_length = 2 * (n - 1)
        time_in_cycle = time % cycle_length

        # If time_in_cycle is less than n, the pillow is moving forward
        if time_in_cycle < n:
            return time_in_cycle + 1
        else:
            # Otherwise, the pillow is moving backward
            return n - (time_in_cycle - (n - 1))
