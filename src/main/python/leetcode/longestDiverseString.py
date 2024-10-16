import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        # Populate the heap with negative counts to simulate a max-heap
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            # Check if we can use this character directly
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break  # No other option available, stop the process
                # Use the next most frequent character instead
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # Decrease the count (since count2 is negative)
                if count2 != 0:
                    heapq.heappush(max_heap, (count2, char2))
                # Push the skipped character back into the heap
                heapq.heappush(max_heap, (count1, char1))
            else:
                # Use the most frequent character
                result.append(char1)
                count1 += 1  # Decrease the count (since count1 is negative)
                if count1 != 0:
                    heapq.heappush(max_heap, (count1, char1))

        return ''.join(result)
