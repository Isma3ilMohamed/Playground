class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the frequency of each string
        frequency = Counter(arr)
        
        # Step 2: Collect distinct strings
        distinct_strings = [string for string in arr if frequency[string] == 1]
        
        # Step 3: Find the k-th distinct string
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""
        
