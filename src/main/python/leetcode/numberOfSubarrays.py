class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of prefix sums
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: to handle subarrays starting from index 0

        current_prefix_sum = 0
        nice_subarrays_count = 0

        for num in nums:
            # Update the current prefix sum (increment if num is odd)
            current_prefix_sum += num % 2

            # Check if there exists a prefix sum that can be subtracted to get k odd numbers
            if current_prefix_sum - k in prefix_sum_count:
                nice_subarrays_count += prefix_sum_count[current_prefix_sum - k]

            # Update the frequency of the current prefix sum
            prefix_sum_count[current_prefix_sum] += 1

        return nice_subarrays_count
