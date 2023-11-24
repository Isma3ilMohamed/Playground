package leetcode

import java.util.*

fun maxCoins(piles: IntArray): Int {
    Arrays.sort(piles)
    var ans=0
    for (i in piles.size/3..<piles.size step 2){
        ans+=piles[i]
    }
    return ans
}

fun main() {
    println(maxCoins(intArrayOf(9,8,7,6,5,1,2,3,4)))
}