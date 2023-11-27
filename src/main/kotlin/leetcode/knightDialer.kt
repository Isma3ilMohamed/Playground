package leetcode

var memo: Array<IntArray> = arrayOf()
var MOD = 1e9.toInt() + 7
var jumps = arrayOf(
    intArrayOf(4, 6),
    intArrayOf(6, 8),
    intArrayOf(7, 9),
    intArrayOf(4, 8),
    intArrayOf(3, 9, 0),
    intArrayOf(),
    intArrayOf(1, 7, 0),
    intArrayOf(2, 6),
    intArrayOf(1, 3),
    intArrayOf(2, 4)
)

fun dp(remain: Int, square: Int): Int {
    if (remain == 0) {
        return 1
    }
    if (memo[remain][square] != 0) {
        return memo[remain][square]
    }
    var ans = 0
    for (nextSquare in jumps[square]) {
        ans = (ans + dp(remain - 1, nextSquare)) % MOD
    }
    memo[remain][square] = ans
    return ans
}

fun knightDialer(n: Int): Int {
    memo = Array(n + 1) { IntArray(10) }
    var ans = 0
    for (square in 0..9) {
        ans = (ans + dp(n - 1, square)) % MOD
    }
    return ans
}

fun main() {
    println(knightDialer(3131))
}