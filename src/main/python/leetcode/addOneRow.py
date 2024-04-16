# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        #base case
        if d==1:
            new_root=TreeNode(v)
            new_root.left=root
            return new_root
        
        # helper function for insertion
        def insert(node,current_depth):
            if not node:
                return
            if current_depth == d-1:
                temp_left=node.left
                node.left=TreeNode(v)
                node.left.left=temp_left

                temp_right=node.right
                node.right=TreeNode(v)
                node.right.right = temp_right
            else:
                insert(node.left,current_depth + 1)
                insert(node.right,current_depth+ 1) 
        insert(root,1)
        return root
