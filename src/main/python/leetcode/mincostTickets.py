class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        For each day/period, look at the 3 options to determine the minimum cost
        cost doesn't guarentee to increase?
        dp[0] = min(cost) or cost[0]
        dp[1:7] = min(cost) or min(cost[0], cost[1]) # 1 or 7 days pass
        dp[i] = min(dp[i], dp[i-6], dp[i-29])
        '''
        # O(366), O(366) or O(d) with d is all days in a year
        traveldays = set(days)
        dp = [0]*366
        for i in range(1,366):
            if i not in traveldays:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[i-1] + costs[0], 
                    dp[i-7] + costs[1] if i >= 7 else costs[1], 
                    dp[i-30] + costs[2] if i >= 30 else costs[2])
        return dp[-1]
