package grokking.fast_slow_pointers;

public class FindDuplicate {
    public static int findDuplicate(int[] nums) {
        int size=nums.length;
        if (size<1){
            return 0;
        }
        int slow=nums[0];
        int fast=nums[nums[0]];
        while (fast != slow){
            slow=nums[slow];
            fast=nums[nums[fast]];
        }
        fast=0;
        while (fast!=slow){
            slow=nums[slow];
            fast=nums[fast];
        }
        return slow;
    }

    public static void main(String[] args) {
        System.out.println(findDuplicate(new int[]{1,3,4,2,2}));
    }
}
