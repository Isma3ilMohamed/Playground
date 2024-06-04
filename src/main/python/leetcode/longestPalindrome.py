class Solution:
    def longestPalindrome(self, s: str) -> int:
        len_s=len(s)
        if s == s[::-1]:
            return len_s
        chars={}
        pd_len=0

        for ch in s:
            if chars.get(ch):
                chars[ch] +=1
                if chars[ch]%2 == 0:
                    pd_len +=2
            else:
                chars[ch]  = 1
        return pd_len +1 if len_s - pd_len != 0 else pd_len
