class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        roots = [i for i in range(n+1)]
        ranks = [1] * (n+1)
        
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            
            return roots[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if ranks[root_x] > ranks[root_y]:
                    roots[root_y] = root_x
                elif ranks[root_x] < ranks[root_y]:
                    roots[root_x] = root_y
                else:
                    roots[root_y] = root_x
                    ranks[root_x] += 1
        
        def is_connected(x, y):
            return find(x) == find(y)

        connections.sort(key=lambda x: x[-1])
        ans = 0
        cnt = 0
        for x, y, cost in connections:
            if not is_connected(x, y):
                union(x, y)
                ans += cost
                cnt += 1
                if cnt == n-1:
                    return ans
        
        return -1
