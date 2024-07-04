class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        current_sum = 0
        node = head.next  # Skip the initial zero node

        while node:
            if node.val != 0:
                current_sum += node.val
            else:
                if current_sum > 0:
                    current.next = ListNode(current_sum)
                    current = current.next
                    current_sum = 0
            node = node.next
        
        return dummy.next
