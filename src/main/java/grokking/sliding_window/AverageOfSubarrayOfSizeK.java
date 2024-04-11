package grokking.sliding_window;

import java.util.Arrays;

public class AverageOfSubarrayOfSizeK {
    public static float [] averageOfSubarrayOfSizeK(int [] nums, int k){
        float [] result = new float[nums.length - k + 1];
        int sum=0;
        int left=0;

        for (int right = 0; right < nums.length; right++) {
            sum +=nums[right];

            if (right >= k-1){
                result[left] = (float) sum / k; // Calculate the average
                sum -= nums[left]; // Remove the element going out of the window
                left++; // Slide the window to the right
            }

        }


        return result;
    }


    public static void main(String[] args) {
        System.out.println(Arrays.toString(averageOfSubarrayOfSizeK(new int[]{1, 3, 2, 6, -1, 4, 1, 8, 2}, 5)));
    }
}
