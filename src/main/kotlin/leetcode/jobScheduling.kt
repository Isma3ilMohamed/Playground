package leetcode

import java.util.*


fun find(i: Int, jobs: Array<IntArray>, startTime: IntArray?, n: Int, dp: IntArray): Int {
    if (i >= n) return 0
    if (dp[i] != -1) return dp[i]
    var index = Arrays.binarySearch(startTime, jobs[i][1])
    if (index < 0) index = -index - 1
    val pick = jobs[i][2] + find(index, jobs, startTime, n, dp)
    val notpick = find(i + 1, jobs, startTime, n, dp)
    dp[i] = Math.max(pick, notpick)
    return dp[i]
}

fun jobScheduling(startTime: IntArray, endTime: IntArray, profit: IntArray): Int {
    val n = profit.size
    val jobs = Array(n) { IntArray(3) }
    val dp = IntArray(n)
    Arrays.fill(dp, -1)
    for (i in 0 until n) {
        jobs[i][0] = startTime[i]
        jobs[i][1] = endTime[i]
        jobs[i][2] = profit[i]
    }
    Arrays.sort(jobs) { j1, j2 ->
        if (j1[0] !== j2[0]) {
            return@sort j1[0] - j2[0]
        } else if (j1[1] !== j2[1]) { // then by end time
            return@sort j1[1] - j2[1]
        } else { //then by profit
            return@sort j2[2] - j1[2]
        }
    }
    Arrays.sort(startTime)
    return find(0, jobs, startTime, n, dp)
}
fun main() {
    println(jobScheduling(intArrayOf(1, 2, 3, 4, 6), intArrayOf(3, 5, 10, 6, 9), intArrayOf(20, 20, 100, 70, 60)))
}