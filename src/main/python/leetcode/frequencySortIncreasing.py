class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequencies of each element
        freq = Counter(nums)
        
        # Sort the array based on the custom key
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums
