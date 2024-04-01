class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_str = s.strip()
        result = 0
        for i in reversed(range(len(trimmed_str))):
            if trimmed_str[i] != " ":
                result += 1
            else:
                break
        return result


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
