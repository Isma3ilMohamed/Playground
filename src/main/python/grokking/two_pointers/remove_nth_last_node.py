from linked_list import LinkedList
from linked_list_node import LinkedListNode


def remove_nth_last_node(head: LinkedList, n: int):
    left = head
    right = head
    for i in range(n):
        right = right.next

    if right is None:
        return head.next
    while right.next is not None:
        right = right.next
        left = left.next

    left.next=left.next.next
    return head
