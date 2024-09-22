class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  # We start from 1, so decrement k by 1

        while k > 0:
            steps = self.get_steps(n, curr, curr + 1)
            if steps <= k:
                # Move to next sibling
                curr += 1
                k -= steps
            else:
                # Move to the first child
                curr *= 10
                k -= 1  # We have moved to next number
        return curr

    def get_steps(self, n, curr, next_curr):
        steps = 0
        while curr <= n:
            steps += min(n + 1, next_curr) - curr
            curr *= 10
            next_curr *= 10
        return steps
