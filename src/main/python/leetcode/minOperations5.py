class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def H(n):
            if n < 0:
                return 0
            s = 0
            power = 1
            while True:
                term = n - (power - 1)
                if term < 0:
                    break
                s += term
                power *= 4
            return s

        total_ans = 0
        for l, r in queries:
            total_work = H(r) - H(l - 1)
            total_ans += (total_work + 1) // 2
        return total_ans
