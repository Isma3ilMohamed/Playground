class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            # Pigeonhole principle: duplicates must exist
            return 0

        minutes_seen = [False] * 1440

        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            total_minutes = hours * 60 + minutes

            if minutes_seen[total_minutes]:
                return 0  # Duplicate time found
            minutes_seen[total_minutes] = True

        # Collect all the times in order
        time_indices = []
        for i in range(1440):
            if minutes_seen[i]:
                time_indices.append(i)

        min_diff = 1440  # Maximum possible difference
        for i in range(1, len(time_indices)):
            diff = time_indices[i] - time_indices[i - 1]
            min_diff = min(min_diff, diff)

        # Compute wrap-around difference
        wrap_around_diff = (time_indices[0] + 1440) - time_indices[-1]
        min_diff = min(min_diff, wrap_around_diff)

        return min_diff
