class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size = len(s)
        s_map = {}
        t_map = {}
        i = 0
        while i < size:
            if (s[i] in s_map and s_map[s[i]] != t[i]) or (t[i] in t_map and t_map[t[i]] != s[i]):
                return False
            else:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
                i += 1
        return True
