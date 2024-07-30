class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        # Prefix and suffix arrays
        prefix_b = [0] * (n + 1)
        suffix_a = [0] * (n + 1)
        
        # Fill prefix_b array
        for i in range(1, n + 1):
            prefix_b[i] = prefix_b[i - 1] + (1 if s[i - 1] == 'b' else 0)
        
        # Fill suffix_a array
        for i in range(n - 1, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (1 if s[i] == 'a' else 0)
        
        # Calculate minimum deletions
        min_deletions = float('inf')
        for i in range(n + 1):
            min_deletions = min(min_deletions, prefix_b[i] + suffix_a[i])
        
        return min_deletions
