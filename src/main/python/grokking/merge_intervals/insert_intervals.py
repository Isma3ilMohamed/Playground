class Solution:
    def insert_intervals(self, existing_intervals: list[list[int]], new_interval: list[int]):
        # First, find the position to insert the new interval to keep the list sorted
        i = 0
        while i < len(existing_intervals) and existing_intervals[i][0] < new_interval[0]:
            i += 1
        existing_intervals.insert(i, new_interval)

        # Now merge overlapping intervals
        merged = []
        for interval in existing_intervals:
            # If the list of merged intervals is empty or there's no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, merge the current interval with the last one in merged
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


solution = Solution()
print(solution.insert_intervals(existing_intervals=[[1,6],[8,9],[10,15],[16,18]], new_interval=[9,10]))
