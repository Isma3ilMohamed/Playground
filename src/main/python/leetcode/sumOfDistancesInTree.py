from typing import List, Dict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # This will hold the size of each subtree and the sum of distances from node u to nodes in its subtree.
        sz = [0] * n
        dp = [0] * n
        # This will hold the final result, the sum of distances from node u to all other nodes.
        ans = [0] * n

        def dfs1(u: int, parent: int):
            """ First DFS to calculate sizes and initial dp values """
            sz[u] = 1
            dp[u] = 0
            for v in graph[u]:
                if v == parent:
                    continue
                dfs1(v, u)
                sz[u] += sz[v]
                dp[u] += dp[v] + sz[v]

        def dfs2(u: int, parent: int):
            """ Second DFS to adjust dp values based on the entire tree """
            ans[u] = dp[u]
            for v in graph[u]:
                if v == parent:
                    continue
                # Move root from u to v
                pu = dp[u]
                pv = dp[v]
                su = sz[u]
                sv = sz[v]

                dp[u] -= dp[v] + sz[v]
                sz[u] -= sz[v]
                dp[v] += dp[u] + sz[u]
                sz[v] += sz[u]

                dfs2(v, u)

                # Restore original values
                dp[u] = pu
                dp[v] = pv
                sz[u] = su
                sz[v] = sv

        # Start DFS from node 0 assuming node 0 is the root.
        dfs1(0, -1)
        dfs2(0, -1)

        return ans

# Example usage:
sol = Solution()
n = 6
edges = [[0,1], [0,2], [2,3], [2,4], [2,5]]
print(sol.sumOfDistancesInTree(n, edges))
