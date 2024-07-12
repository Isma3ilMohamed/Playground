class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, substr, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] + char == substr:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(char)
            return ''.join(stack), total_score

        # Determine the order of removal
        if x > y:
            s, score1 = remove_substring(s, 'ab', x)
            s, score2 = remove_substring(s, 'ba', y)
        else:
            s, score1 = remove_substring(s, 'ba', y)
            s, score2 = remove_substring(s, 'ab', x)

        return score1 + score2
