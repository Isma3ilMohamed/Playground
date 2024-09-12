from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert the allowed characters into a set for fast lookups
        allowed_set = set(allowed)
        
        # Count how many words are consistent
        consistent_count = 0
        
        # Iterate through each word in the list
        for word in words:
            if all(char in allowed_set for char in word):
                consistent_count += 1
        
        return consistent_count
