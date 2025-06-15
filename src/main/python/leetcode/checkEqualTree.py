class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        r_list = []
        def dfs(root):
            if not root:
                return 0 
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            total = root.val + left_sum +right_sum
            r_list.append(total)
            return total

        total_sum = dfs(root)
        r_list.pop()
        if total_sum %2 != 0:
            return False
        
        
        return (total_sum//2) in r_list
