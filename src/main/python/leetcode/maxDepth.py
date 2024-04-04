class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_counter = 0

        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1

            max_counter=max(max_counter,counter)

        return max_counter


soluiton = Solution()
print(soluiton.maxDepth("(1)+((2))+(((3)))"))
