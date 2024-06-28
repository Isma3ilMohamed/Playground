class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Calculate the degree of each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Step 2: Sort cities by their degree in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign importance based on sorted degree
        importance = [0] * n
        for i in range(n):
            importance[sorted_cities[i]] = n - i
        
        # Step 4: Calculate the total importance of the roads
        total_importance = 0
        for a, b in roads:
            total_importance += importance[a] + importance[b]
        
        return total_importance
