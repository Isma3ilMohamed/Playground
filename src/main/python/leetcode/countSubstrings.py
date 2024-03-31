class Solution:

    def countSubstrings(self, s: str) -> int:
        ans = 0

        def extendPalindrome(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        if s == "": return 0

        for i in range(len(s)):
            even = extendPalindrome(s, i, i)
            odd = extendPalindrome(s, i, i + 1)
            ans += even + odd
        return ans
