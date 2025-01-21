class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = ans = 0
        freq = {}  # Dictionary to track the frequency of characters in the window
        for right in range(len(s)):
            # Add the current character to the frequency dictionary
            freq[s[right]] = freq.get(s[right], 0) + 1

            # If the number of distinct characters is more than 2, shrink the window
            while len(freq) > 2:
                # Decrease the frequency of the left character
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]  # Remove the character from the dictionary if its count is 0
                left += 1

            # Calculate the maximum length of the valid substring
            ans = max(ans, right - left + 1)

        return ans
s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct(s="ccaabbb"))