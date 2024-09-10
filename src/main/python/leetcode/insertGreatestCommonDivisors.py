class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse through the linked list
        while current and current.next:
            # Calculate GCD of current node and next node
            gcd_value = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            gcd_node = ListNode(gcd_value)
            
            # Insert the new node between current and current.next
            gcd_node.next = current.next
            current.next = gcd_node
            
            # Move two steps ahead (to skip over the inserted GCD node)
            current = gcd_node.next
        
        return head
