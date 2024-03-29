package grokking.fast_slow_pointers;

public class CircularArray {

    public static boolean circularArrayLoop(int[] nums) {

        int size=nums.length;
        for (int i = 0; i < size; i++) {
            int slow=i,fast=i;
            boolean forward=nums[i]>0;
            while (true){
                slow=nextStep(slow,nums[slow],size);

                if (isNotCycle(nums,forward,slow)){
                    break;
                }
                fast=nextStep(fast,nums[fast],size);
                if (isNotCycle(nums,forward,fast)){
                    break;
                }
                fast=nextStep(fast,nums[fast],size);
                if (isNotCycle(nums,forward,fast)){
                    break;
                }
                if (slow==fast){
                    return true;
                }
            }

        }
        return false;
    }

    // A function to calculate the next step
    public static int nextStep(int pointer, int value, int size) {
        int result = (pointer + value) % size;
        if (result < 0)
            result += size;
        return result;
    }
    public static boolean isNotCycle(int [] nums,boolean prevDirection,int pointer){
        boolean currDirection=nums[pointer]>= 0;
        return prevDirection != currDirection || Math.abs(nums[pointer] % nums.length) == 0;
    }
    public static void main(String[] args) {
        System.out.println(circularArrayLoop(new int[]{1,3,-2,-4,1}));
    }

}
