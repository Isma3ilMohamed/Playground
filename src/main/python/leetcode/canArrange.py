from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import Counter

        freq = Counter()
        for num in arr:
            remainder = num % k
            freq[remainder] += 1

        for r in range(k):
            if r == 0:
                # Remainder 0 must have even count
                if freq[r] % 2 != 0:
                    return False
            elif k % 2 == 0 and r == k // 2:
                # When k is even, remainder k/2 must have even count
                if freq[r] % 2 != 0:
                    return False
            else:
                # Count of remainder r must match count of remainder k - r
                if freq[r] != freq[k - r]:
                    return False

        return True
