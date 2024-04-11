package grokking.sliding_window;

public class MinimumSubArraySum {
    public static int minSubArrayLen(int target, int[] nums) {
        int windowSize = Integer.MAX_VALUE;
        int currSubArrSize = 0;
        int start = 0;
        int sum = 0;

        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            while (sum >= target) {
                currSubArrSize = (end + 1) - start;
                windowSize = Math.min(windowSize, currSubArrSize);
                sum -= nums[start];
                start += 1;
            }
        }

        if (windowSize != Integer.MAX_VALUE) {
            return windowSize;
        }
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(minSubArrayLen(7,new int[]{2,3,1,2,4,3}));
    }
}
