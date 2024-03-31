def climbStairs(n: int) -> int:
    prev_prev = 1
    prev = 2
    for i in range(2, n + 1):
        prev, prev_prev = prev + prev_prev, prev
    return prev_prev


print(climbStairs(6))
