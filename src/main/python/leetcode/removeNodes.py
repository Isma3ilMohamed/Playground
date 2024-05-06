# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python.leetcode.helper import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        current = stack.pop()
        max = current.val
        result_list = ListNode(max)

        while stack:
            current = stack.pop()
            if current.val < max:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                max = current.val

        return result_list
