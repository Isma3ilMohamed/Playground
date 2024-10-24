class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Base case: If both nodes are None, they are equivalent
        if not root1 and not root2:
            return True
        
        # If one of them is None or values are different, they are not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Recursively check two conditions:
        # 1. Non-flipped: Compare left-left and right-right
        # 2. Flipped: Compare left-right and right-left
        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right)) or (
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
