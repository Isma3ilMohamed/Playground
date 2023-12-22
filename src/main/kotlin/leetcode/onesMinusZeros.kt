package leetcode

import java.util.*

fun onesMinusZeros(grid: Array<IntArray>): Array<IntArray>? {
    val m = grid.size
    val n = grid[0].size
    val onesRow = IntArray(m)
    val onesCol = IntArray(n)
    Arrays.fill(onesRow, 0)
    Arrays.fill(onesCol, 0)
    for (i in 0..<m) {
        for (j in 0..<n) {
            onesRow[i] += grid[i][j]
            onesCol[j] += grid[i][j]
        }
    }
    val diff = Array(m) { IntArray(n) }
    for (i in 0..<m) {
        for (j in 0..<n) {
            diff[i][j] = 2 * onesRow[i] + 2 * onesCol[j] - n - m
        }
    }
    return diff
}