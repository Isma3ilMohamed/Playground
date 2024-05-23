def count_beautiful_subsets(nums, k):
    def backtrack(start, path):
        # Sum the current subset
        subset_sum = sum(path)
        # If the sum is divisible by k, it's a beautiful subset
        if subset_sum % k == 0 and len(path) > 0:
            beautiful_subsets.append(list(path))
        
        # Try including each number in the subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    beautiful_subsets = []
    backtrack(0, [])
    return len(beautiful_subsets)
