class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            
            parent_node = nodes[parent_val]
            child_node = nodes[child_val]
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child_val)

        root = None
        for node_val in nodes:
            if node_val not in children:
                root = nodes[node_val]
                break

        return root
