class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(x, y):
            # Check if the subgrid contains exactly the numbers 1 to 9
            s = set()
            for i in range(3):
                for j in range(3):
                    s.add(grid[x + i][y + j])
            if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            
            # Check the sum of rows, columns, and diagonals
            sum1 = grid[x][y] + grid[x][y + 1] + grid[x][y + 2]
            sum2 = grid[x + 1][y] + grid[x + 1][y + 1] + grid[x + 1][y + 2]
            sum3 = grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]
            if sum1 != sum2 or sum2 != sum3:
                return False
            
            sum4 = grid[x][y] + grid[x + 1][y] + grid[x + 2][y]
            sum5 = grid[x][y + 1] + grid[x + 1][y + 1] + grid[x + 2][y + 1]
            sum6 = grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2]
            if sum4 != sum5 or sum5 != sum6:
                return False
            
            sum7 = grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2]
            sum8 = grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y]
            if sum7 != sum8:
                return False
            
            return True
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        
        return count
