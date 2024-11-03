class Solution:
    def rotateString(self,s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s_double = s + s
        return goal in s_double
        
