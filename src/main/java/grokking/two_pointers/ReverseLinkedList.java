package grokking.two_pointers;

import grokking.helpers.LinkedListNode;
import grokking.helpers.LinkedList;



public class ReverseLinkedList {
    public static LinkedListNode removeNthLastNode(LinkedListNode head, int n) {
        LinkedListNode left = head,right = head;

        for (int i = 0; i < n; i++) {
            right=right.next;
        }

        if (right==null){
            return head.next;
        }
        while (right.next!=null){
            right=right.next;
            left=left.next;
        }

        left.next=left.next.next;

        return head;
    }

    public static void main(String[] args) {
        LinkedList<Integer> linkedList =new LinkedList<Integer>();
        linkedList.createLinkedList(new int[]{23,28,10,5,67,39,70,28});
        linkedList.printListWithForwardArrow(removeNthLastNode(linkedList.head,2));
    }
}
