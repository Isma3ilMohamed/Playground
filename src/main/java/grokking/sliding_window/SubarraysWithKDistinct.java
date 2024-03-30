package grokking.sliding_window;

import java.util.HashMap;
import java.util.Map;

public class SubarraysWithKDistinct {

    public static int subarraysWithKDistinct(int[] nums, int k) {
        return slidingWindowAtMost(nums,k) - slidingWindowAtMost(nums,k-1);
    }

    private static int slidingWindowAtMost(int[] nums,int k){
        Map<Integer,Integer> freqMap= new HashMap<>();
        int left=0;
        int totalCount=0;

        for (int right = 0; right < nums.length; right++) {
            freqMap.put(nums[right],freqMap.getOrDefault(nums[right],0)+1);

            while (freqMap.size()>k){
                freqMap.put(nums[left], freqMap.getOrDefault(nums[left],0)-1);
                if (freqMap.get(nums[left])==0){
                    freqMap.remove(nums[left]);
                }
                left++;
            }
            totalCount +=(right-left+1);
        }

        return totalCount;
    }

    public static void main(String[] args) {
        System.out.println(subarraysWithKDistinct(new int[]{1,2,1,2,3},2));
    }
}
