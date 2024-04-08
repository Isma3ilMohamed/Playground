package grokking.sliding_window;

import java.util.HashMap;

public class FindLongestSubstring {
    public static int findLongestSubstring(String str) {
        HashMap<Character ,Integer> window=new HashMap<>();
        int left =0;
        int result=0;
        for (int right = 0; right < str.length(); right++) {
            if (window.containsKey(str.charAt(right))){
                left =Math.max(window.get(str.charAt(right))+1, left);
            }
            window.put(str.charAt(right), right);
            result=Math.max(result, right - left +1);
        }

        return result;
    }
}
