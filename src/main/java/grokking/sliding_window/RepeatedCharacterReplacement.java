package grokking.sliding_window;

import java.util.HashMap;
import java.util.Map;

public class RepeatedCharacterReplacement {
    public static int longestRepeatingCharacterReplacement(String s, int k) {
        int mostFreqChar=0;
        int lengthOfMaxSubstring=0;
        int start=0;
        int stringLength=s.length();

        Map<Character,Integer> charCount = new HashMap<>();
        // iterate over the input string
        for (int end = 0; end < stringLength; ++end) {
            char currentChar=s.charAt(end);
            // if the new character is not in the hash map, add it, else increment its frequency
            charCount.put(currentChar,charCount.getOrDefault(currentChar,0)+1);
            // update the most frequent char
            mostFreqChar=Math.max(mostFreqChar,charCount.get(currentChar));

            // if the number of replacements in the current window have exceeded the limit, slide the window
            if (end - start+1-mostFreqChar>k){
                charCount.put(s.charAt(start),charCount.get(s.charAt(start))-1);
                start++;
            }
            // if this window is the longest so far, update the length of max substring
            lengthOfMaxSubstring=Math.max(lengthOfMaxSubstring,end-start+1);
        }

        // return the length of the max substring with same characters after replacement(s)
        return lengthOfMaxSubstring;
    }


    public static void main(String[] args) {
        System.out.println(longestRepeatingCharacterReplacement("aabccbb",2));
    }
}
