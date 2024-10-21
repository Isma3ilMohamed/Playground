class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function to perform backtracking
        def backtrack(start, seen):
            # If we've reached the end of the string, return the number of unique substrings
            if start == len(s):
                return len(seen)
            
            max_splits = 0
            # Try splitting the string at every possible point
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                # Only recurse if this substring hasn't been seen before
                if substring not in seen:
                    seen.add(substring)  # Add the current substring to the set
                    max_splits = max(max_splits, backtrack(end, seen))  # Recurse
                    seen.remove(substring)  # Backtrack and remove the substring from the set
            return max_splits

        # Start the backtracking process from index 0 with an empty set
        return backtrack(0, set())
