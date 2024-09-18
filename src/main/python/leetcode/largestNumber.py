from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert numbers to strings
        nums_str = [str(num) for num in nums]
        
        # Step 2: Define a custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # x and y are equal in terms of ordering
        
        # Step 3: Sort the string numbers using the custom comparator
        nums_str.sort(key=functools.cmp_to_key(compare))
        
        # Step 4: Handle leading zeros
        if nums_str[0] == '0':
            return '0'
        
        # Step 5: Concatenate sorted numbers
        largest_number = ''.join(nums_str)
        return largest_number
