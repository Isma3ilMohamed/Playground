package leetcode

fun findSpecialInteger(arr: IntArray): Int {
    val counts: MutableMap<Int, Int> = HashMap()
    val target = arr.size / 4
    for (num in arr) {
        counts[num] = counts.getOrDefault(num, 0) + 1
        if (counts[num]!! > target) {
            return num
        }
    }
    return -1
}