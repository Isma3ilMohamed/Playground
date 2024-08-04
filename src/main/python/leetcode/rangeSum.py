class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        subarray_sums = []
        
        # Generate all subarray sums and store them in the heap
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Calculate the sum from the 'left' to 'right' (1-indexed, so adjust indices by -1)
        return sum(subarray_sums[left-1:right]) % mod
