class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert the nums list into a set for O(1) lookups
        nums_set = set(nums)
        
        # Create a dummy node to handle edge cases like deleting the head node
        dummy = ListNode(0)
        dummy.next = head
        
        # Start traversing from the dummy node
        current = dummy
        
        while current and current.next:
            if current.next.val in nums_set:
                # Skip the node that needs to be removed
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the modified linked list
        return dummy.next
