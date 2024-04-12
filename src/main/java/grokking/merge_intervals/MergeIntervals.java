package grokking.merge_intervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class MergeIntervals {

    public static int[][] mergeIntervals(int[][] intervals) {
        List<int[]> output = new ArrayList<>();

        int lastEditedPosition = 0;
        output.add(intervals[lastEditedPosition]);

        for (int i = 1; i < intervals.length; i++) {
            int[] temp = intervals[i];
            // [1,9],[3,8]
            if (output.get(lastEditedPosition)[0] <= temp[0] && temp[0] <= output.get(lastEditedPosition)[1]) {
                int resultX = Math.min(temp[0], output.get(lastEditedPosition)[0]);
                int resultY = Math.max(temp[1], output.get(lastEditedPosition)[1]);
                output.set(lastEditedPosition, new int[]{resultX, resultY});
            } else {
                lastEditedPosition++;
                output.add(temp);
            }
        }

        return listToArray(output);
    }
    public static int[][] listToArray(List<int[]> list) {
        // Create a new 2D array with the same size as the list
        int[][] array = new int[list.size()][];

        // Copy each int[] from the list into the new 2D array
        for (int i = 0; i < list.size(); i++) {
            array[i] = list.get(i);
        }

        return array;
    }

    public static void main(String[] args) {
        int[][] input = new int[3][2];
        input[0] = new int[]{1, 9};
        input[1] = new int[]{3, 8};
        input[2] = new int[]{4, 4};
        System.out.println(Arrays.deepToString(mergeIntervals(input)));
    }
}

