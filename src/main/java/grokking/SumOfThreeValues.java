package grokking;

import java.util.Arrays;

public class SumOfThreeValues {
    public static boolean findSumOfThree(int[] nums, int target) {
        Arrays.sort(nums);
        int low,high,triplet=0;

        for (int i = 0; i < nums.length - 2; i++) {
            low=i+1;
            high=nums.length-1;

            while (low<high){
                triplet=nums[low] + nums[high] + nums[i];

                if (triplet==target){
                    return true;
                }else if (triplet < target){
                    low++;
                }else{
                    high--;
                }
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int [] nums= new int[5];

        System.out.println(findSumOfThree(new int[]{3,7,1,2,8,4,5},10));
    }
}
