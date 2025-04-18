class Solution:
    def countAndSay(self, n: int) -> str:
        from collections import Counter
        def rle(s):
            ans = ''
            curr = s[0]
            count = 1
            for char in s[1:]:
                if char == curr:
                    count += 1
                else:
                    ans = f"{ans}{count}{curr}"
                    curr = char
                    count = 1
            ans = f"{ans}{count}{curr}"
            return ans
        
        op = "1"
        for _ in range(n-1):
            op = rle(op)
        return op



        
