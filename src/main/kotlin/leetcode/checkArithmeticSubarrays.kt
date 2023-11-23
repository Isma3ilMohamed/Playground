package leetcode

import java.util.*
import kotlin.collections.ArrayList

fun check(arr: IntArray): Boolean {
    Arrays.sort(arr)
    val diff = arr[1] - arr[0]
    for (i in 2..<arr.size) {
        if (arr[i] - arr[i - 1] != diff) {
            return false
        }
    }
    return true
}

fun checkArithmeticSubarrays(nums: IntArray, l: IntArray, r: IntArray): MutableList<Boolean?> {
    val ans: MutableList<Boolean?> = ArrayList()
    for (i in l.indices) {
        val arr = IntArray(r[i] - l[i] + 1)
        for (j in arr.indices) {
            arr[j] = nums[l[i] + j]
        }
        ans.add(check(arr))
    }
    return ans
}