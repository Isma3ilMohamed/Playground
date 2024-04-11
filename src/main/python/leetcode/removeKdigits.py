class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        if k==0:
            return num
        stack=[]
        for i in range(len(num)):
            ch=num[i]
            while len(stack)!=0 and k>0 and stack[-1]>ch:
                stack.pop()
                k-=1
            stack.append(ch)
        for j in range(k):
            stack.pop()
        result=[]
        while len(stack)!=0:
            result.append(stack.pop())
        result=''.join(result[::-1])
        while len(result)>1 and result[0]=='0':
            result=result[1:]
        return result
