package leetcode

import java.util.*

fun findContentChildren(g: IntArray, s: IntArray): Int {
    g.sort()
    s.sort()
    var i = 0
    var j = 0
    while (i < g.size && j < s.size) {
        if (s[j] >= g[i])
            i+=1
        j+=1
    }
    return i
}

fun main() {
    println(findContentChildren(intArrayOf(1,2,3), intArrayOf(1,1)))
}