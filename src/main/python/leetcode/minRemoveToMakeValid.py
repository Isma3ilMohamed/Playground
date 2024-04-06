class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices_to_remove = set()
        stack = []

        # First pass: Identify invalid parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    indices_to_remove.add(i)

        # Add remaining open parentheses in the stack to indices_to_remove
        indices_to_remove = indices_to_remove.union(set(stack))

        # Construct the result string
        result = ''.join([s[i] for i in range(len(s)) if i not in indices_to_remove])

        return result


solution = Solution()
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
