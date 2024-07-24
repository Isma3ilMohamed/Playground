class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        # Create a list of tuples (mapped_value, original_value)
        mapped_nums = [(map_number(num), num) for num in nums]
        
        # Sort based on the mapped_value
        mapped_nums.sort(key=lambda x: x[0])
        
        # Extract the sorted original values
        sorted_nums = [original for mapped, original in mapped_nums]
        
        return sorted_nums
