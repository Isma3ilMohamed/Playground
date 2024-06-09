class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of remainders
        remainder_count = defaultdict(int)
        # Initialize with remainder 0 to handle subarrays starting from the beginning
        remainder_count[0] = 1
        
        cumulative_sum = 0
        count = 0
        
        for num in nums:
            # Update the cumulative sum
            cumulative_sum += num
            # Compute the remainder
            remainder = cumulative_sum % k
            # Ensure the remainder is non-negative
            if remainder < 0:
                remainder += k
            
            # If the remainder is already in the map, it means there are subarrays
            # that sum up to a multiple of k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            # Update the count of this remainder in the map
            remainder_count[remainder] += 1
        
        return count
