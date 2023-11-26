package leetcode

import java.util.*

fun largestSubmatrix(matrix: Array<IntArray>): Int {
    val m = matrix.size
    val n = matrix[0].size
    var ans = 0
    for (row in 0..<m) {
        for (col in 0..<n) {
            if (matrix[row][col] != 0 && row > 0) {
                matrix[row][col] += matrix[row - 1][col]
            }
        }
        val currRow = matrix[row].clone()
        Arrays.sort(currRow)
        for (i in 0..<n) {
            ans = Math.max(ans, currRow[i] * (n - i))
        }
    }
    return ans
}