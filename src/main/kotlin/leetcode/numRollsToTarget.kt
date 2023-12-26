package leetcode

import java.util.Arrays


val mod = Math.pow(10.0,9.0) + 7
fun numRollsToTarget(n: Int, k: Int, target: Int): Int {
    val dp = Array(n + 1) { IntArray(target + 1) }
    for (d in dp){
        Arrays.fill(d,-1)
    }
    return recursiveCall(dp, n, k, target)
}

fun recursiveCall(dp:Array<IntArray>,n:Int,k:Int,target:Int):Int{
    if (target==0 && n == 0) return 1
    if (n==0 || target <= 0) return 0

    if (dp[n][target] != -1) return (dp[n][target]% mod).toInt()
    var ways=0
    for (i in 1..k){
        ways=((ways+ recursiveCall(dp,n-1,k,target-i)) % mod).toInt()
    }
    dp[n][target] = (ways % mod).toInt()
    return dp[n][target]
}

fun main() {
    println(numRollsToTarget(1,6,3))
}