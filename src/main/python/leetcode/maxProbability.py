class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Build the graph
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        # Priority queue with (-probability, node)
        max_heap = [(-1.0, start)]
        # Probability to reach each node, initialized to 0
        prob = [0.0] * n
        prob[start] = 1.0
        
        while max_heap:
            current_prob, node = heappop(max_heap)
            current_prob = -current_prob  # convert back to positive
            
            # If we reached the end node, return the probability
            if node == end:
                return current_prob
            
            # Explore neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = current_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0  # If end node is not reachable
