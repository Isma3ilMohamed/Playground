class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def resolves(a,b,Operator):
            if Operator == '+':
                return a+b
            elif Operator == "-":
                return a-b
            elif Operator == "*":
                return a*b
            return int(a/b)
        
        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                int2=stack.pop()
                int1=stack.pop()
                operator = token
                resolver_ans=resolves(int1,int2,operator)
                stack.append(resolver_ans)
            else:
                stack.append(int(token))
        
        return stack.pop()
