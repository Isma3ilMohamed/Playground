class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        cur_sum, result = 0, 0
        start, end = 0, 0
        seen = {}
        pref_sum = [0] * (n + 1)
        
        for end in range(n):  
            pref_sum[end + 1] = pref_sum[end] + nums[end]
            
            if nums[end] in seen:
                start = max(seen[nums[end]] + 1, start)
                
            result = max(result, pref_sum[end + 1] - pref_sum[start])
            seen[nums[end]] = end
                         
        return result
