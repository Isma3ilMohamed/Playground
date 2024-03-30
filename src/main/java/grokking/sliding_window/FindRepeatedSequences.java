package grokking.sliding_window;

import java.util.*;

public class FindRepeatedSequences{

    //AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT k=10
    public static Set<String> findRepeatedSequences(String s, int k) {

        int subStringLengthLimit=s.length()-k;
        Map<String ,Integer> sequenceCount=new HashMap<>();

        Set<String> relatedSequence = new HashSet<>();

        for (int i = 0; i <= subStringLengthLimit ; i++) {
            String currentSequence=s.substring(i,i+k);
            sequenceCount.put(currentSequence,sequenceCount.getOrDefault(currentSequence,0)+1);

            if (sequenceCount.get(sequenceCount) >= 2){
                relatedSequence.add(currentSequence);
            }
        }

        return relatedSequence;
    }
}