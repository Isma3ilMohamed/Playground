# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:

        curr = head
        while curr is not None:

            for _ in range(m - 1):
                if curr is None:
                    break
                curr = curr.next
            if curr is None:
                break

            tail = curr
            for _ in range(n + 1):
                if curr is None:
                    break
                curr = curr.next

            if curr is None:
                tail.next = None
                break

            tail.next = curr

        return head
