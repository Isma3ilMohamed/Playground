package grokking.helpers;

import java.util.*;

// Template for the linked list
public class LinkedList<T> {
    public LinkedListNode head;

    // constructor will be used to make a LinkedList type object
    public LinkedList() {
        this.head = null;
    }

    // insertNodeAtHead method will insert a LinkedListNode at head
    // of a linked list.
    public void insertNodeAtHead(LinkedListNode node) {
        if (this.head == null) {
            this.head = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
    }

    // createLinkedList method will create the linked list using the
    // given integer array with the help of InsertAthead method.
    public void createLinkedList(int[] lst) {
        for (int i = lst.length - 1; i >= 0; i--) {
            LinkedListNode newNode = new LinkedListNode(lst[i]);
            insertNodeAtHead(newNode);
        }
    }

    public void printListWithForwardArrow(LinkedListNode head) {
        LinkedListNode temp = head;

        while (temp != null) {
            System.out.print(temp.data); // print node value
            temp = temp.next;
            if (temp != null) {
                System.out.print(" → ");
            }
        }
        // if this is the last node, print null at the end
        System.out.print(" → null ");
    }

    // returns the node at the specified position(index) of the linked list
    public static LinkedListNode getNode(LinkedListNode head, int pos) {
        LinkedListNode ptr = head;
        if (pos != -1) {
            int p = 0;

            while (p < pos) {
                ptr = ptr.next;
                p += 1;
            }

            return ptr;
        }
        return ptr;
    }

    // returns the number of nodes in the linked list
    public static int getLength(LinkedListNode head) {
        LinkedListNode temp = head;
        int count = 0;
        while (temp != null) {
            count++;
            temp = temp.next;
        }
        return count;
    }

    public static LinkedListNode reverseLinkedList(LinkedListNode slowPtr){
        LinkedListNode prev = null;
        LinkedListNode next = null;
        LinkedListNode curr = slowPtr;

        while (curr != null)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static boolean compareTwoHalves(LinkedListNode firstHalf, LinkedListNode secondHalf) {
        while (firstHalf != null && secondHalf != null) {
            if (firstHalf.data != secondHalf.data) {
                return false;
            } else {
                firstHalf = firstHalf.next;
                secondHalf = secondHalf.next;
            }


        }
        return true;
    }
}