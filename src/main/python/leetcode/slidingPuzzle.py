class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        q = deque([])
        final_state = '123450'
        cur_state = ''
        for row in board:
            for v in row:
                cur_state += str(v)
    
        can_move_to = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        visited = set()
        q.append((cur_state, 0, cur_state.index('0'))) # cur_state, steps, zero_pos
        while q:
            cur_state, steps, zero_pos = q.popleft()
            if cur_state == final_state:
                return steps

            
            for available_space in can_move_to[zero_pos]:
                new_state = list(cur_state)
                new_state[zero_pos], new_state[available_space] = new_state[available_space], new_state[zero_pos]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, steps + 1, available_space))
        return -1 
