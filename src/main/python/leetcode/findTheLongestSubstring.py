class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to their respective bit positions
        vowel_to_bit = {'a': 1 << 0,
                        'e': 1 << 1,
                        'i': 1 << 2,
                        'o': 1 << 3,
                        'u': 1 << 4}

        state_to_index = {0: -1}  # Initial state with index -1
        state = 0                 # Initial bitmask state
        max_length = 0

        for i, c in enumerate(s):
            # If the character is a vowel, toggle its bit in the state
            if c in vowel_to_bit:
                state ^= vowel_to_bit[c]

            # If the state has been seen before, update max_length
            if state in state_to_index:
                length = i - state_to_index[state]
                max_length = max(max_length, length)
            else:
                # Record the first occurrence of this state
                state_to_index[state] = i

        return max_length
