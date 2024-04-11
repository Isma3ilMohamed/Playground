package grokking.sliding_window;

public class MaxSubArraySum {

    public static int maxSubArraySum(int [] nums,int target){

        int maxSum=0;
        int windowSum=0;

        int start=0;

        for (int end = 0; end < nums.length; end++) {
            windowSum += nums[end];

            if (end>= target-1){
                maxSum= Math.max(maxSum,windowSum);
                windowSum -= nums[start];
                start++;
            }
        }

        return maxSum;

    }

    public static void main(String[] args) {
        System.out.println(maxSubArraySum(new int[]{2, 1, 5, 1, 3, 2},3));
    }
}
