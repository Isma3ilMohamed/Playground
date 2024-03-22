# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=[]
        while head is not None:
            ans.append(head.val)
            head=head.next
        return True if ans == ans[::-1] else False
