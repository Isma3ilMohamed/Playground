package leetcode


fun findDiagonalOrder(nums: List<List<Int>>): IntArray {
    var n = 0
    var i = 0
    var maxKey = 0
    val map: MutableMap<Int, MutableList<Int>> = HashMap()
    for (r in nums.size - 1 downTo 0) { // The values from the bottom rows are the starting values of the diagonals.
        for (c in 0..<nums[r].size) {
            map.putIfAbsent(r + c, ArrayList())
            map[r + c]!!.add(nums[r][c])
            maxKey = Math.max(maxKey, r + c)
            n++
        }
    }
    val ans = IntArray(n)
    for (key in 0..maxKey) {
        val value = map[key] ?: continue
        for (v in value) ans[i++] = v
    }
    return ans
}

fun main() {

}