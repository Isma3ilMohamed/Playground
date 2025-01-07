class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in range(len(words)):
            for w in words : 
                if w  in words[i] and w != words[i]:
                    ans.add(w)
        return list(ans)            
            
        
