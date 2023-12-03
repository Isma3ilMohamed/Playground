package leetcode

fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
    var ans = 0
    for (i in 0..<points.size - 1) {
        val currX = points[i][0]
        val currY = points[i][1]
        val targetX = points[i + 1][0]
        val targetY = points[i + 1][1]
        ans += Math.max(Math.abs(targetX - currX), Math.abs(targetY - currY))
    }
    return ans
}