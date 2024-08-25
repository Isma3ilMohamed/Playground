package grokking.merge_intervals;

import grokking.merge_intervals.helper.Interval;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class EmployeeFreeTime {
    public static List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> ans = new ArrayList<Interval>();
        List<Interval> allIntervals = new ArrayList<Interval>();

        for (List<Interval> intervals : schedule){
            allIntervals.addAll(intervals);
        }

        //Sort
        allIntervals.sort((a, b) -> a.start != b.start ? a.start - b.start : a.end - b.end);

        Interval prev=null;
        for (Interval current:allIntervals){
            if (prev==null || current.start> prev.end){
                if (prev!=null){
                    ans.add(new Interval(prev.end,current.start));
                }
                prev=current;
            }else{
                prev.end=Math.max(prev.end, current.end);
            }
        }
        return ans;
    }
}
