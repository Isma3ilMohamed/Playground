class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flip = [0] * n
        flip_count = 0
        result = 0

        for i in range(n):
            if i >= K:
                flip_count ^= flip[i - K]
            
            if A[i] == flip_count:
                if i + K > n:
                    return -1
                flip[i] = 1
                flip_count ^= 1
                result += 1

        return result
