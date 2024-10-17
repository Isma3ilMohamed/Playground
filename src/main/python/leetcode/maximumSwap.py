class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to a list of digits
        digits = list(str(num))
        
        # Create a dictionary to store the last occurrence of each digit
        last = {int(d): i for i, d in enumerate(digits)}

        # Traverse through each digit in the number
        for i, d in enumerate(digits):
            # Check if a larger digit exists after the current one
            for digit in range(9, int(d), -1):
                if last.get(digit, -1) > i:
                    # Swap the current digit with the larger digit
                    digits[i], digits[last[digit]] = digits[last[digit]], digits[i]
                    # Return the new number after the swap
                    return int(''.join(digits))

        # If no swap could improve the number, return the original number
        return num
