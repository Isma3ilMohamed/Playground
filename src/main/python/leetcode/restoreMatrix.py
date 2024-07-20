class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                min_val = min(rowSum[i], colSum[j])
                result[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        
        return result
