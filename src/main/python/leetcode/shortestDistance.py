from collections import deque
import sys


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        # Next four directions
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(grid)
        cols = len(grid[0])

        # Total matrix to store total distance sum for each empty cell
        total = [[0 for _ in range(cols)] for _ in range(rows)]

        emptyLandValue = 0
        minDist = sys.maxsize

        for row in range(rows):
            for col in range(cols):

                # Start a bfs from each house
                if grid[row][col] == 1:
                    minDist = sys.maxsize

                    # Use a queue to perform a BFS, starting from the cell located at (row, col)
                    q = deque([(row, col)])

                    steps = 0

                    while q:
                        steps += 1

                        for _ in range(len(q)):
                            curr = q.popleft()

                            for dir in dirs:
                                nextRow = curr[0] + dir[0]
                                nextCol = curr[1] + dir[1]

                                # For each cell with the value equal to empty land value
                                # add distance and decrement the cell value by 1
                                if (
                                    0 <= nextRow < rows
                                    and 0 <= nextCol < cols
                                    and grid[nextRow][nextCol] == emptyLandValue
                                ):
                                    grid[nextRow][nextCol] -= 1
                                    total[nextRow][nextCol] += steps

                                    q.append((nextRow, nextCol))
                                    minDist = min(minDist, total[nextRow][nextCol])

                    # Decrement empty land value to be searched in next iteration
                    emptyLandValue -= 1

        return -1 if minDist == sys.maxsize else minDist
