from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions correspond to: north (0, 1), east (1, 0), south (0, -1), west (-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the position and direction
        x, y = 0, 0  # Robot starts at (0, 0)
        direction = 0  # Initially facing north
        
        # Convert obstacles to a set of tuples for fast lookup
        obstacle_set = set(map(tuple, obstacles))
        
        max_distance_sq = 0  # Maximum distance squared from the origin
        
        for command in commands:
            if command == -2:  # Turn left (counterclockwise)
                direction = (direction - 1) % 4
            elif command == -1:  # Turn right (clockwise)
                direction = (direction + 1) % 4
            else:
                # Move forward in the current direction
                for _ in range(command):
                    new_x = x + directions[direction][0]
                    new_y = y + directions[direction][1]
                    if (new_x, new_y) not in obstacle_set:
                        x, y = new_x, new_y
                        # Update the max distance squared
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        break  # Stop moving in this direction if there's an obstacle
        
        return max_distance_sq
