# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.leetcode.helper import TreeNode


class Solution:
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     def isLeaf(node):
    #         return node is not None and not node.left and not node.right
    #
    #     left_sum = 0
    #     if root.left and isLeaf(root.left):
    #         left_sum = root.left.val
    #     else:
    #         left_sum = self.sumOfLeftLeaves(root.left)
    #
    #     right_sum = self.sumOfLeftLeaves(root.right)
    #
    #     return left_sum + right_sum
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, left):

            if not node:
                return 0

            if not node.left and not node.right:
                if left:
                    return node.val
                else:
                    return 0

            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root.left, True) + dfs(root.right, False)