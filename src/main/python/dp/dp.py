cache = {}


# Fib Example
def fib(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result


def fib_bottom_up(n):
    meme = {}
    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = meme[i - 1] + meme[i - 2]
        meme[i] = result
    return meme[n]


# print(fib_bottom_up(50))


# Minimum Coins Problem Example
def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


# memo = {}
#
#
# def min_coins(m, coins):
#     if m in memo:
#         return memo[m]
#     if m == 0:
#         answer = 0
#     else:
#         answer = None
#         for coin in coins:
#             subproblem = m - coin
#
#             if subproblem < 0:
#                 # Skip solutions where we try to reach [m]
#                 # from a negative subproblem
#                 continue
#             answer = min_ignore_none(answer, min_coins(subproblem, coins) + 1)
#     memo[m] = answer
#     return answer


def min_coins_bottom_up(m, coins):
    memo = {0: 0}
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return memo[m]


# Many ways to construct coins
from collections import defaultdict


def many_ways_coins_bottom_up(m, coins):
    memo = defaultdict(lambda _: 0)
    memo[0] = 1
    for i in range(1, m + 1):
        memo[i] = 0

        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = memo[i] + memo[subproblem]
    return memo[m]


# print(many_ways_coins_bottom_up(87, [1, 4, 5, 8]))


# Maze Problem

def grid_paths(n, m):
    memo = {}

    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
    return memo[(n, m)]


# print(grid_paths(18,6))
print(grid_paths(75, 19))

# Key takeaways
# 1) Define the subproblem
# 2) What's the base case?
# 3) find recursive formula for general solution
