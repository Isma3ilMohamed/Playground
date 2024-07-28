class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Priority queue to store (current_time, current_node, num_visits)
        pq = [(0, 1, 0)]
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        
        while pq:
            current_time, node, num_visits = heappop(pq)
            
            for neighbor in graph[node]:
                next_time = current_time + time
                # Calculate the wait time due to traffic light changes
                if (current_time // change) % 2 == 1:
                    next_time += change - (current_time % change)
                
                if next_time < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = next_time
                    heappush(pq, (next_time, neighbor, num_visits + 1))
                elif dist[neighbor][0] < next_time < dist[neighbor][1]:
                    dist[neighbor][1] = next_time
                    heappush(pq, (next_time, neighbor, num_visits + 1))
        
        return dist[n][1]
