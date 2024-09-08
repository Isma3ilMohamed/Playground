class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = length // k
        extra = length % k  # The first 'extra' parts will have one extra node
        
        # Step 3: Split the list
        result = []
        current = head
        
        for i in range(k):
            part_head = current  # The start of this part
            # Determine the size of this part
            current_part_size = part_size + (1 if i < extra else 0)
            
            # Move 'current' to the end of this part
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Break the link if needed
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            # Add this part to the result
            result.append(part_head)
        
        # If we have fewer nodes than 'k', append None to result
        while len(result) < k:
            result.append(None)
        
        return result
