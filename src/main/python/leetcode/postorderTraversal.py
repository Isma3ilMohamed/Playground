class Solution:
    def postorderTraversal(self,root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        list = []
        stack = []
        stack.append(root)
        
        while stack:
            root = stack.pop()
            list.append(root.val)  # Append to the end of the list
            
            # Push left before right to ensure right is processed first
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        # Since we added root before its children, reverse the list to get postorder
        return list[::-1]
