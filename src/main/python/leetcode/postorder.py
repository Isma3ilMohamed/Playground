"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self,root: 'Node') -> list[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            # Add children to stack; they will be processed in reverse order
            stack.extend(node.children)

        return result[::-1]  # Reverse the result list to get the correct postorder