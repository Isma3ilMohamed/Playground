class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2):
            return False
        
        # Initialize character counts
        s1_count = [0] * 26  # For 'a' to 'z'
        s2_count = [0] * 26  # For the current window in s2
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] +=1
            s2_count[ord(s2[i]) - ord('a')] +=1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches +=1
        
        # Slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Index of the character to add
            index = ord(s2[r]) - ord('a')
            s2_count[index] +=1
            if s1_count[index] == s2_count[index]:
                matches +=1
            elif s1_count[index] +1 == s2_count[index]:
                matches -=1
            
            # Index of the character to remove
            index = ord(s2[l]) - ord('a')
            s2_count[index] -=1
            if s1_count[index] == s2_count[index]:
                matches +=1
            elif s1_count[index] -1 == s2_count[index]:
                matches -=1
            l +=1
        
        return matches == 26
