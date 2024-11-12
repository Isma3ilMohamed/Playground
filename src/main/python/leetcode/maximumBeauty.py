from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price, then by beauty
        items.sort()
        
        # Sort queries but remember their original indices
        indexed_queries = sorted((price, i) for i, price in enumerate(queries))
        
        results = [0] * len(queries)  # To store final results in the original order
        max_beauty = 0
        item_index = 0
        
        # Process each query in sorted order
        for query_price, original_index in indexed_queries:
            # Move item pointer to include all items affordable under the current query's price
            while item_index < len(items) and items[item_index][0] <= query_price:
                max_beauty = max(max_beauty, items[item_index][1])  # Update max beauty
                item_index += 1
            
            # Store the maximum beauty for this query in the original index
            results[original_index] = max_beauty

        return results
