class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for ch in expression:
            if ch == 't':
                stack.append(True)
            elif ch == 'f':
                stack.append(False)
            elif ch in ['!', '&', '|']:
                stack.append(ch)
            elif ch == ')':
                sub_expr = []
                # Pop elements until the operator is found
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove the '('
                
                operator = stack.pop()  # Get the operator ('!', '&', '|')
                
                # Apply the operator to the sub-expression
                if operator == '!':
                    # There is only one element to negate
                    result = not sub_expr[0]
                elif operator == '&':
                    # All elements must be True for AND
                    result = all(sub_expr)
                elif operator == '|':
                    # At least one element must be True for OR
                    result = any(sub_expr)
                
                # Push the result of the evaluated expression back onto the stack
                stack.append(result)
            elif ch == '(':
                stack.append('(')
        
        # The final result is the last element in the stack
        return stack[-1]
