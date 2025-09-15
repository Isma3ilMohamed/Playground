class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sen=text.split()
        cnt=0
        for i in range(len(sen)):
            not_word=0
            for j in range(len(brokenLetters)):
                if brokenLetters[j]  in sen[i]:
                    not_word=1
                    break
            if not_word==0:
                cnt+=1
        return cnt
        
