class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        res = s.split(" ")
        return len(res[-1])


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
