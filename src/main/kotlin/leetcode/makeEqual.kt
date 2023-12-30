package leetcode

import java.util.HashMap

fun makeEqual(words: Array<String>): Boolean {
    val count= hashMapOf<Char,Int>()
    for (word in words){
        word.toCharArray().forEach {
            count[it] = count.getOrDefault(it,0)+1
        }
    }
    for (c in count.keys){
        if ((count[c]?.toInt()?.rem(words.size) ?: 0) != 0){
            return false
        }
    }

    return true

}

fun main() {
    println(makeEqual(arrayOf("abc","aabc","bc")))
}