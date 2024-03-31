class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1,-1,-1):
            curr_temp=temperatures[i]

            while stack and curr_temp >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1] -i

            stack.append(i)
        return result
