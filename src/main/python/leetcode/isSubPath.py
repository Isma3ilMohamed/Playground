class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Helper function to check if there's a match starting from this tree node
        def dfs(tree_node, list_node):
            if not list_node:  # If we reached the end of the list, it's a match
                return True
            if not tree_node:  # If the tree node is None and the list isn't done, return False
                return False
            if tree_node.val != list_node.val:  # If values don't match, return False
                return False
            # Check both left and right subtrees
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
        
        if not root:
            return False
        
        # Check if the linked list starts from this root, or any of its subtrees
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
