package grokking.merge_intervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class IntervalsIntersection {
    public static int[][] intervalsIntersection(int[][] intervalLista, int[][] intervalListb) {
        List<int[]> result = new ArrayList<>();
        int i = 0, j = 0;

        while (i < intervalLista.length && j < intervalListb.length) {
            // Find the start and end of the intersection
            int startMax = Math.max(intervalLista[i][0], intervalListb[j][0]);
            int endMin = Math.min(intervalLista[i][1], intervalListb[j][1]);

            // Check if there is an intersection
            if (startMax <= endMin) {
                result.add(new int[]{startMax, endMin});
            }

            // Move the pointer that has the interval with the smaller end time
            if (intervalLista[i][1] < intervalListb[j][1]) {
                i++;
            } else {
                j++;
            }
        }

        // Convert list of arrays to 2D array
        return result.toArray(new int[result.size()][]);
    }


    public static void main(String[] args) {
        int[][][] inputIntervalLista = {
/*                {{1, 2}},
                {{1, 4}, {5, 6}, {9, 15}},
                {{3, 6}, {8, 16}, {17, 25}},
                {{4, 7}, {9, 16}, {17, 28}, {39, 50}, {55, 66}, {70, 89}},*/
                {{1, 3}, {5, 6}, {7, 8}, {12, 15}}
        };

        int[][][] inputIntervalListb = {
/*                {{1, 2}},
                {{2, 4}, {5, 7}, {9, 15}},
                {{2, 3}, {10, 15}, {18, 23}},
                {{3, 6}, {7, 8}, {9, 10}, {14, 19}, {23, 33}, {35, 40}, {45, 59}, {60, 64}, {68, 76}},*/
                {{2, 4}, {7, 10}}
        };

        for (int i = 0; i < inputIntervalLista.length; i++) {
            System.out.println(Arrays.deepToString(intervalsIntersection(inputIntervalLista[i], inputIntervalListb[i])));
        }

    }
}
