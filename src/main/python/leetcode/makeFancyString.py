class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty list to build the result
        result = []
        
        # Iterate through each character in the string
        for char in s:
            # Check if the last two characters in result are the same as the current char
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue  # Skip adding this character to avoid three consecutive same characters
            result.append(char)  # Otherwise, add the character to the result list
        
        # Join the list into a string and return
        return ''.join(result)
