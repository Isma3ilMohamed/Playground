from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        t=m*n
        if len(original) !=t:
            return []
        result = []
        for i in range(m):
            s=i*n
            e=s+n
            result.append(original[s:e])
        
        return result
        
