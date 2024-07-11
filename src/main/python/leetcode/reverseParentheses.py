class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # This will hold the characters within the current set of parentheses
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis
                if stack:
                    stack.pop()
                # Reverse the characters and push them back onto the stack
                stack.extend(temp)
            else:
                stack.append(char)
        
        return ''.join(stack)
