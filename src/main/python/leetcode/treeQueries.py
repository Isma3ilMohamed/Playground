class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Dictionary to store the height of each node
        node_height = {}
        
        # Dictionary to store the level of each node
        node_level = {}
        
        # Dictionary to store all heights at each level
        level_heights = defaultdict(list)
        
        # Step 1: DFS to calculate the height and level of each node
        def dfs(node, level):
            if not node:
                return -1
            left_height = dfs(node.left, level + 1)
            right_height = dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)
            
            # Store height and level of the current node
            node_height[node.val] = current_height
            node_level[node.val] = level
            level_heights[level].append(current_height)
            
            return current_height
        
        # Initialize DFS to calculate heights and levels
        dfs(root, 0)
        
        # Sort heights in each level in descending order for easy access
        for level in level_heights:
            level_heights[level].sort(reverse=True)
        
        # Step 2: Process each query
        result = []
        for query in queries:
            level = node_level[query]
            height_of_query_node = node_height[query]
            
            # Determine new height at this level after removing the query node's subtree
            if len(level_heights[level]) == 1:
                # If the query node is the only node at this level
                new_height = level - 1
            else:
                # If there are multiple nodes at this level
                if level_heights[level][0] == height_of_query_node:
                    # If the query node has the maximum height, use the second-highest height
                    new_height = level + level_heights[level][1]
                else:
                    # Otherwise, use the maximum height for this level
                    new_height = level + level_heights[level][0]
            
            result.append(new_height)
        
        return result
