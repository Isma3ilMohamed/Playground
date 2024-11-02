class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Check each word with the next word in sequence
        for i in range(len(words) - 1):
            # If the last character of the current word does not match the first of the next word, return False
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check the circular condition between the last word and the first word
        return words[-1][-1] == words[0][0]
