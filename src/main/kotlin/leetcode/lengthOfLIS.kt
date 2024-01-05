package leetcode

fun lengthOfLIS(nums: IntArray): Int {
    val tails = IntArray(nums.size)
    var size = 0
    for (x in nums) {
        var i = 0
        var j = size
        while (i != j) {
            val m = (i + j) / 2
            if (tails[m] < x) i = m + 1 else j = m
        }
        tails[i] = x
        if (i == size) ++size
    }
    return size
}