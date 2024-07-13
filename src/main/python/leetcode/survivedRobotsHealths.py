class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        stack = []

        for i in range(len(positions)):
            pos, health, direction = positions[i], healths[i], directions[i]
            
            if direction == 'R':
                stack.append((pos, health, direction))
            else:  # direction == 'L'
                while stack and stack[-1][2] == 'R':
                    prev_pos, prev_health, prev_direction = stack.pop()
                    
                    if prev_health > health:
                        prev_health -= 1
                        health = 0
                        stack.append((prev_pos, prev_health, prev_direction))
                        break
                    elif prev_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                
                if health > 0:
                    stack.append((pos, health, direction))

        return [health for pos, health, direction in stack]
