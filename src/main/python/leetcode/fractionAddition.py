from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Parse the expression
        fractions = []
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                sign = -1 if expression[i] == '-' else 1
                i += 1
            
            j = i
            while j < len(expression) and expression[j] != '+' and expression[j] != '-':
                j += 1
            
            num, den = map(int, expression[i:j].split('/'))
            fractions.append(Fraction(sign * num, den))
            i = j
        
        # Add up all fractions
        result = sum(fractions, Fraction(0, 1))
        
        # Simplify the result
        numerator, denominator = result.numerator, result.denominator
        gcd_value = gcd(abs(numerator), denominator)
        
        return f"{numerator // gcd_value}/{denominator // gcd_value}"
