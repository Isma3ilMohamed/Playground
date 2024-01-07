package leetcode

fun numberOfArithmeticSlices(nums: IntArray): Int {
    val n = nums.size
    var total_count = 0
    val dp: Array<HashMap<Int, Int>?> = arrayOfNulls(n)
    for (i in 0 until n) {
        dp[i] = HashMap()
    }
    for (i in 1 until n) {
        for (j in 0 until i) {
            val diff = nums[i].toLong() - nums[j]
            if (diff > Int.MAX_VALUE || diff < Int.MIN_VALUE) {
                continue
            }
            val diffInt = diff.toInt()
            dp[i]!![diffInt] = dp[i]!!.getOrDefault(diffInt, 0) + 1
            if (dp[j]!!.containsKey(diffInt)) {
                dp[i]!![diffInt] = dp[i]!![diffInt]!! + dp[j]!![diffInt]!!
                total_count += dp[j]!![diffInt]!!
            }
        }
    }
    return total_count
}