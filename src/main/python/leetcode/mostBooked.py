class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return 0

        meetings.sort()

        meeting_count = [0] * n

        busy = []
        available = [i for i in range(n)]

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if not available:
                prev_end, room = heapq.heappop(busy)
                # 5), (1, 4) -> (5, 8)
                heapq.heappush(busy, (end - start + prev_end, room))
            else:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            
            meeting_count[room] += 1

        return meeting_count.index(max(meeting_count))
