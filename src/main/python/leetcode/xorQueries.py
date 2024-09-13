from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Compute the prefix XOR array
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        # Step 2: Answer each query
        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix[r])  # If l == 0, we just take prefix[r]
            else:
                result.append(prefix[r] ^ prefix[l - 1])  # Use prefix XOR
        
        return result
