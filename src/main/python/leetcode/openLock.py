class Solution:
    def openLock(self,deadends, target):
        deadends = set(deadends)  # To quickly check if a state is a deadend
        queue = deque([('0000', 0)])  # (state, steps)
        visited = set('0000')
        
        if '0000' in deadends:
            return -1

        while queue:
            state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            for i in range(4):
                for move in (-1, 1):  # Moving the dial up or down
                    new_digit = (int(state[i]) + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    if new_state not in visited and new_state not in deadends:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
        
        return -1
        
