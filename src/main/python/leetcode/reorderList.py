# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Two pointer technique to get middle of linked list
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
        
        # Reverse from middle to end of linked list
        middle = slow
        fast = slow
        slow = None
        while fast:
            nextNode = fast.next
            fast.next = slow
            slow = fast
            fast = nextNode
        
        # Merge 2 linked list to desired ordered linked list
        first = head
        second = slow
        node = None
        while first and first != middle:
            nextOfFirst = first.next

            if node: node.next = first
            first.next = second
            node = second

            first = nextOfFirst
            second = second.next
