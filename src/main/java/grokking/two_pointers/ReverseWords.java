package grokking.two_pointers;

import java.util.ArrayList;
import java.util.Arrays;

public class ReverseWords {
    public static String reverseWords(String sentence) {
        String [] reversed = sentence.replaceAll("\\s+", " ").trim().split(" ");
        int left=0;
        int right=reversed.length-1;
        while (left<right){
            if (reversed[left]=="  " || reversed[right]==" "){
                left++;
                right--;
                continue;
            }
            String temp=reversed[left];
            reversed[left]=reversed[right];
            reversed[right]=temp;
            left++;
            right--;
        }
        return String.join(" ",reversed);
    }

    public static void main(String[] args) {
        System.out.println(reverseWords("Hello     World"));
    }
}
