from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Extract and sort unique elements
        unique_elements = sorted(set(arr))
        
        # Step 2: Create a mapping from element to rank
        element_to_rank = {}
        for rank, element in enumerate(unique_elements, start=1):
            element_to_rank[element] = rank
        
        # Step 3: Transform the original array
        ranked_arr = [element_to_rank[element] for element in arr]
        
        return ranked_arr
