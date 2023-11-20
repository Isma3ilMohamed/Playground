package leetcode

fun garbageCollection(garbage: Array<String>, travel: IntArray): Int {
    val n = garbage.size
    var ans = 0
    for (i in 0..<n - 1) {
        ans += 3 * travel[i]
    }
    for (s in garbage) {
        ans += s.length
    }
    for (i in n - 1 downTo 1) {
        ans -= if (!garbage[i].contains("G")) {
            travel[i - 1]
        } else {
            break
        }
    }
    for (i in n - 1 downTo 1) {
        ans -= if (!garbage[i].contains("P")) {
            travel[i - 1]
        } else {
            break
        }
    }
    for (i in n - 1 downTo 1) {
        ans -= if (!garbage[i].contains("M")) {
            travel[i - 1]
        } else {
            break
        }
    }
    return ans
}
fun main() {
    println(garbageCollection(arrayOf("G","P","GP","GG"), intArrayOf(2,4,3)))
}