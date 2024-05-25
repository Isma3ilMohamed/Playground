class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(start: int) -> List[str]:
            if start in memo:
                return memo[start]

            results = []
            if start == len(s):
                results.append("")
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sentence in backtrack(end):
                        if sentence:
                            results.append(word + " " + sentence)
                        else:
                            results.append(word)
            
            memo[start] = results
            return results
        
        wordSet = set(wordDict)
        memo = {}
        return backtrack(0)
