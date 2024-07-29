class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        count = 0
        
        # Loop over each soldier as the middle soldier of the triplet
        for j in range(1, n-1):
            left_less = left_greater = right_less = right_greater = 0
            
            # Count soldiers to the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            # Count soldiers to the right of j
            for k in range(j+1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                elif rating[k] < rating[j]:
                    right_less += 1
            
            # Count valid teams
            count += left_less * right_greater + left_greater * right_less
        
        return count
