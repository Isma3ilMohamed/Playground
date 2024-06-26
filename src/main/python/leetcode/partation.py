class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start,path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start+1,len(s)+1):
                prefix=s[start:end]
                if is_palindrome(prefix):
                    backtrack(end,path+[prefix])
        
        result = []
        backtrack(0,[])
        return result
