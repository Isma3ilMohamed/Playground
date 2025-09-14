class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Create sets and dictionaries for different matching levels
        exact_words = set(wordlist)
        case_map = {}  # lowercase -> first occurrence in wordlist
        vowel_map = {}  # vowel pattern -> first occurrence in wordlist
        
        def to_vowel_pattern(word):
            """Convert word to pattern where all vowels are replaced with '*'"""
            word_lower = word.lower()
            pattern = []
            for ch in word_lower:
                if ch in 'aeiou':
                    pattern.append('*')
                else:
                    pattern.append(ch)
            return ''.join(pattern)
        
        # Build the maps (process wordlist in order to maintain first occurrence)
        for word in wordlist:
            word_lower = word.lower()
            
            # Store first occurrence for case-insensitive match
            if word_lower not in case_map:
                case_map[word_lower] = word
            
            # Store first occurrence for vowel pattern match
            vowel_pattern = to_vowel_pattern(word)
            if vowel_pattern not in vowel_map:
                vowel_map[vowel_pattern] = word
        
        # Process queries
        result = []
        for query in queries:
            # Check exact match first (highest priority)
            if query in exact_words:
                result.append(query)
                continue
            
            # Check case-insensitive match
            query_lower = query.lower()
            if query_lower in case_map:
                result.append(case_map[query_lower])
                continue
            
            # Check vowel error match
            vowel_pattern = to_vowel_pattern(query)
            if vowel_pattern in vowel_map:
                result.append(vowel_map[vowel_pattern])
                continue
            
            # No match found
            result.append("")
        
        return result

