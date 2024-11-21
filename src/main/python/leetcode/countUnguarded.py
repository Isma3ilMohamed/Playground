class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[0] * n for _ in range(m)]
        
        # Constants for marking the grid
        GUARD, WALL, GUARDED = -1, -2, 1
        
        # Mark guards and walls on the grid
        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL
        
        # Simulate guard coverage in all directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in {GUARD, WALL}:
                    if grid[nr][nc] == 0:  # Only mark unvisited cells as guarded
                        grid[nr][nc] = GUARDED
                    nr += dr
                    nc += dc
        
        # Count unguarded cells
        unguarded_count = 0
        for row in grid:
            unguarded_count += row.count(0)  # Count all cells that are neither guarded nor occupied
        
        return unguarded_count
