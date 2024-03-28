package grokking.fast_slow_pointers;

import grokking.helpers.LinkedList;
import grokking.helpers.LinkedListNode;

public class CycleDetection {
    public static boolean detectCycle(LinkedListNode head) {
        if (head == null) {
            return false;
        }

        LinkedListNode slow = head;
        LinkedListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LinkedList<Integer> linkedList =new LinkedList<Integer>();
        linkedList.createLinkedList(new int[]{23,28,10,5,67,39,70,28});
    }
}
