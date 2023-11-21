package leetcode

fun countNicePairs(nums: IntArray): Int {
    var res = 0
    val mod = Math.pow(10.0, 9.0).toInt() + 7
    val count: MutableMap<Int, Int> = HashMap()
    for (n in nums) {
        val rev = rev(n)
        val cur = count.getOrDefault(n - rev, 0)
        count[n - rev] = cur + 1
        res = (res + cur) % mod
    }
    return res
}

private fun rev(num: Int): Int {
    var num = num
    var reversedNum = 0
    while (num > 0) {
        val digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num /= 10
    }
    return reversedNum
}

fun main() {

}