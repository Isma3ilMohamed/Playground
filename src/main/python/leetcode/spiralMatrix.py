
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the m x n matrix with -1s
        matrix = [[-1] * n for _ in range(m)]
        
        # Boundaries for the spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Pointer to traverse the linked list
        current = head
        
        while current:
            # Fill from left to right
            for col in range(left, right + 1):
                if current:
                    matrix[top][col] = current.val
                    current = current.next
            top += 1  # Move the top boundary down

            # Fill from top to bottom
            for row in range(top, bottom + 1):
                if current:
                    matrix[row][right] = current.val
                    current = current.next
            right -= 1  # Move the right boundary left

            # Fill from right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if current:
                        matrix[bottom][col] = current.val
                        current = current.next
                bottom -= 1  # Move the bottom boundary up

            # Fill from bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if current:
                        matrix[row][left] = current.val
                        current = current.next
                left += 1  # Move the left boundary right
        
        return matrix
