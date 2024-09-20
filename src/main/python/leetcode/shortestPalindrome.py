# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         # Idea: truncate reversed version as much as possible
#         rev = s[::-1]
#         for i in range(len(rev)):
#             curr = rev[:i] + s
#             if curr == curr[::-1]:
#                 return curr
#         return rev + s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Step 1: Construct the temporary string
        temp = s + '#' + s[::-1]

        # Step 2: Compute the LPS array
        lps = self.computeLPSArray(temp)

        # Step 3: Form the shortest palindrome
        # Length of the longest palindromic prefix
        longest_pal_pref_len = lps[-1]
        # Suffix that needs to be added in front
        suffix_to_add = s[longest_pal_pref_len:]
        # Reverse the suffix and prepend
        shortest_palindrome = suffix_to_add[::-1] + s

        return shortest_palindrome

    def computeLPSArray(self, pattern):
        length = 0
        lps = [0] * len(pattern)
        # Start from the second character
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                    # Do not increment i here
                else:
                    lps[i] = 0
                    i += 1
        return lps
