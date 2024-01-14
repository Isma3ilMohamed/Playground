package leetcode

import java.util.*

fun closeStrings(word1: String, word2: String): Boolean {
    val freq1=IntArray(26)
    val freq2=IntArray(26)

    for (ch in word1.toCharArray()){
        freq1[ch-'a']++
    }
    for (ch in word2.toCharArray()){
        freq2[ch-'a']++
    }

    for (i in 0..< 26){
        if ((freq1[i]==0 && freq2[i]!=0) || (freq1[i]!=0 && freq2[i]==0)){
            return false
        }
    }

    Arrays.sort(freq1)
    Arrays.sort(freq2)

    for (i in 0..< 26){
        if (freq1[i] != freq2[i]) {
            return false;
        }
    }

    return true
}

fun main() {
    println(closeStrings("a","aa"))
}