class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][atom] += count

        result = ""
        for atom in sorted(stack[-1]):
            result += atom
            if stack[-1][atom] > 1:
                result += str(stack[-1][atom])

        return result
