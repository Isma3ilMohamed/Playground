class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack:
                top = stack[-1]
                if (top == 'A' and c == 'B') or (top == 'C' and c == 'D'):
                    stack.pop()  # Remove the substring "AB" or "CD"
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)
