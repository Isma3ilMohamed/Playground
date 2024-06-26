
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: In-order traversal to get sorted list of nodes
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST from sorted list of nodes
        def build_balanced_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = nodes[mid]
            node.left = build_balanced_bst(left, mid - 1)
            node.right = build_balanced_bst(mid + 1, right)
            return node
        
        return build_balanced_bst(0, len(nodes) - 1)
