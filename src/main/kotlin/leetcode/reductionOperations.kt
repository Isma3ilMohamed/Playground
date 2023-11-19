package leetcode

import java.util.*

fun reductionOperations(nums: IntArray): Int {
    Arrays.sort(nums)
    var ans = 0
    for (i in nums.size - 1 downTo 1) {
        if (nums[i - 1] != nums[i]) {
            ans += nums.size - i
        }
    }
    return ans
}
fun main() {

    println(reductionOperations(intArrayOf(5,1,3)))

}