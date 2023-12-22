package leetcode

fun largestOddNumber(num: String): String {
    if (num[num.length - 1].code % 2 == 1) return num
    var i = num.length - 1
    while (i >= 0) {
        val n = num[i].code
        if (n % 2 == 1) return num.substring(0, i + 1)
        i--
    }
    return ""
}
fun main() {
    println(largestOddNumber("35427"))
}