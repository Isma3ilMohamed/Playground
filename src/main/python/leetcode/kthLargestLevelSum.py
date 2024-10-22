class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        
        # Use a queue to perform BFS
        queue = deque([root])
        level_sums = []

        # Perform level-order traversal
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Traverse all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val  # Add the node's value to the level sum
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Store the sum of the current level
            level_sums.append(level_sum)
        
        # Sort the sums in descending order
        level_sums.sort(reverse=True)
        
        # Check if k is within bounds
        if k > len(level_sums):
            return -1
        
        # Return the k-th largest sum
        return level_sums[k - 1]
