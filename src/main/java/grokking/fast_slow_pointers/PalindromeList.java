package grokking.fast_slow_pointers;

import grokking.helpers.LinkedList;
import grokking.helpers.LinkedListNode;

public class PalindromeList {
    public static boolean palindrome(LinkedListNode head) {
        LinkedListNode slow=head;
        LinkedListNode fast=head;
        while (fast!=null && fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }
        LinkedListNode reversed= LinkedList.reverseLinkedList(slow);
        boolean check = LinkedList.compareTwoHalves(head,reversed);

        return check;
    }

    public static void main(String[] args) {
        LinkedList<Integer> linkedList =new LinkedList<Integer>();
        linkedList.createLinkedList(new int[]{1,2,3,2,1});
        System.out.println(palindrome(linkedList.head));
    }
}
