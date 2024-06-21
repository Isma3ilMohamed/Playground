class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total_satisfied = 0
        
        # Calculate initial satisfied customers
        for i in range(n):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        
        # Calculate the additional customers satisfied by the secret technique
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        # Initial window
        for i in range(X):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
        max_additional_satisfied = current_additional_satisfied
        
        # Slide the window
        for i in range(X, n):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            if grumpy[i - X] == 1:
                current_additional_satisfied -= customers[i - X]
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        return total_satisfied + max_additional_satisfied
