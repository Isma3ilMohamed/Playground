class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string to a number by converting each character to its corresponding number
        converted_number = ''
        for char in s:
            converted_number += str(ord(char) - ord('a') + 1)
        
        # Step 2: Sum the digits k times
        for _ in range(k):
            converted_number = sum(int(digit) for digit in converted_number)
            converted_number = str(converted_number)
        
        # The final result is the number after k transformations
        return int(converted_number)
        
