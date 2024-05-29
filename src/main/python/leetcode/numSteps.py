class Solution:
    def numSteps(self, s):
        n = int(s,2)
        a = 0
        while n>1:
            if n &1: n+=1
            else: n//=2
            a+=1
        return a
