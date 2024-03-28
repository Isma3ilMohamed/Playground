package grokking.fast_slow_pointers;

import grokking.helpers.LinkedListNode;

public class MiddleNode {
    public static LinkedListNode middleNode(LinkedListNode head) {
        if (head.next==null){
            return head;
        }
        LinkedListNode fast=head;
        LinkedListNode slow=head;
        while (fast!=null && fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }

        return slow;
    }
}
