from typing import List
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Dictionary to store normalized row forms
        row_patterns = Counter()
        
        for row in matrix:
            # Normalize the row: if the first element is 1, flip the row
            normalized = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            row_patterns[normalized] += 1
        
        # Return the maximum count of rows that can be made identical
        return max(row_patterns.values())
