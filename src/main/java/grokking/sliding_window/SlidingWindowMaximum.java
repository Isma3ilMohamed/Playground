package grokking.sliding_window;

import java.util.*;

class SlidingWindowMaximum {
    public static int[] findMaxSlidingWindow(int[] nums, int w) {
        int[] result = new int[nums.length - w + 1];

        for (int i = 0; i < nums.length; i++) {
            if (w + i <= nums.length) {
                result[i] = splitIntArrayAndFindMax(nums, i, w + i);
            }

        }


        return result;
    }

    public static int splitIntArrayAndFindMax(int[] array, int startIndex, int endIndex) {
        int max=array[startIndex];
        for (int i = startIndex; i < endIndex ; i++) {
            if (array[i]>max){
                max=array[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(findMaxSlidingWindow(new int[]{10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67}, 3)));
    }
}