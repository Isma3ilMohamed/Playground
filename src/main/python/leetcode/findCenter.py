class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Extract the nodes from the first edge
        node1, node2 = edges[0]
        
        # Check which of these nodes appears in the second edge
        if node1 in edges[1]:
            return node1
        else:
            return node2
