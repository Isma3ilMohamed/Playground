package grokking.merge_intervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class InsertInterval {
    public static int[][] insertInterval(int[][] existingIntervals, int[] newInterval) {

        List<int[]> output = new ArrayList<>(Arrays.asList(existingIntervals));
        int new_interval_index=0;

        while(new_interval_index<existingIntervals.length && existingIntervals[new_interval_index][0] < newInterval[0]){
            new_interval_index++;
        }
        output.add(new_interval_index,newInterval);

        // Now merge overlapping intervals
        List<int[]> merged = new ArrayList<>();
        for (int[] interval : output) {
            // If the list of merged intervals is empty or there's no overlap
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
                merged.add(interval);
            } else {
                // There is an overlap, merge the current interval with the last one in merged
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
            }
        }

        return merged.toArray(new int[merged.size()][]);

    }

    public static void main(String[] args) {
        int[][] input = new int[4][2];
        input[0] = new int[]{1, 6};
        input[1] = new int[]{8, 9};
        input[2] = new int[]{10, 15};
        input[3] = new int[]{16, 18};
        System.out.println(Arrays.deepToString(insertInterval(input, new int[]{9, 10})));
    }
}
