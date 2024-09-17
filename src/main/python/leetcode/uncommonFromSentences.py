from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Step 2: Split sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()
        
        # Step 3: Combine word lists
        all_words = words_s1 + words_s2
        
        # Step 4: Count word frequencies
        word_counts = Counter(all_words)
        
        # Step 5: Identify uncommon words
        uncommon_words = [word for word, count in word_counts.items() if count == 1]
        
        # Step 6: Return the result
        return uncommon_words
