class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Base case: when there's only one player (0-indexed)
        
        # Iterate from 2 to n to compute the position for each number of players
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        return winner + 1  # Convert 0-indexed to 1-indexed
