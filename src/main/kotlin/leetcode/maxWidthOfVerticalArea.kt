package leetcode

import java.util.*

fun maxWidthOfVerticalArea(points: Array<IntArray>): Int {

    Arrays.sort(points) { a, b -> a[0].compareTo(b[0]) }
    var result = 0
    for (i in 1..<points.size) {
        result = Math.max(result, points[i][0] - points[i - 1][0])
    }
    return result
}