from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Step 1: Initialize a cache for memoization
        memo = {}

        # Step 2: Define the recursive function
        def ways(expr):
            # Step 3: Check for memoized results
            if expr in memo:
                return memo[expr]

            # Step 4: Base case
            if expr.isdigit():
                memo[expr] = [int(expr)]
                return memo[expr]

            res = []
            # Step 5: Iterate over the expression
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Split the expression into left and right parts
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])

                    # Step 5.1: Combine the results
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)

            # Step 6: Store and return the results
            memo[expr] = res
            return res

        return ways(expression)
