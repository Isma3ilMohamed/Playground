class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            
            if not node.left and not node.right:
                # It's a leaf node
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count pairs
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.result += 1
            
            # Increment distances by 1 for the parent call
            return [d + 1 for d in left_distances + right_distances]
        
        self.result = 0
        dfs(root)
        return self.result
