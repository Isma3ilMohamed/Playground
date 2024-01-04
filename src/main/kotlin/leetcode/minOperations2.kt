package leetcode


val cache= hashMapOf<Int,Int>()
fun minOperations(nums: IntArray): Int {
    var res=0
    val counter = HashMap<Int, Int>()
    for (num in nums) {
        counter[num] = counter.getOrDefault(num, 0) + 1
    }
    for (c in counter.values) {
        if (c == 1) {
            return -1
        }
        res += Math.ceil(c.toDouble() / 3).toInt()
    }
    return res
}
fun main() {
println(minOperations(intArrayOf(2,3,3,2,2,4,2,3,4)))
}