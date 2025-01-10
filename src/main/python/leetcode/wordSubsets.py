class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d={}
        ans=set(words1)
        for i in words2:
            for j in i:
                count=i.count(j)
                if j not in d or count>d[j]:
                    d[j]=count
        for word in words1:
            for j in d:
                if word.count(j)<d[j]:
                    ans.remove(word)
                    break
        return list(ans)
