from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True

            grid2[r][c] = 0  # Mark this cell as visited
            is_sub_island = grid1[r][c] == 1  # This cell is a sub-island only if it's also land in grid1

            # Explore all 4 directions
            is_sub_island &= dfs(r + 1, c)
            is_sub_island &= dfs(r - 1, c)
            is_sub_island &= dfs(r, c + 1)
            is_sub_island &= dfs(r, c - 1)

            return is_sub_island

        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        count += 1

        return count
