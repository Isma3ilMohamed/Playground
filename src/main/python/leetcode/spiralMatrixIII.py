class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1  # Initial step size
        result = [[r0, c0]]
        x, y = r0, c0  # Starting point
        d = 0  # Initial direction index

        while len(result) < R * C:
            for _ in range(2):
                dx, dy = directions[d]
                for _ in range(steps):
                    x, y = x + dx, y + dy
                    if 0 <= x < R and 0 <= y < C:
                        result.append([x, y])
                d = (d + 1) % 4  # Change direction
            
            steps += 1  # Increment step size every two turns

        return result
