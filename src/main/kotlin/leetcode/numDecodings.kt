package leetcode

fun numDecodings(s: String): Int {
    val n = s.length
    if (n == 0) {
        return 0
    }
    var first = 1
    var second = if (isValid(s[0].code - '0'.code, 1)) 1 else 0
    for (i in 2..n) {
        var ans = 0
        if (isValid(s[i - 1].code - '0'.code, 1)) {
            ans += second
        }
        if (isValid((s[i - 2].code - '0'.code) * 10 + s[i - 1].code - '0'.code, 2)) {
            ans += first
        }
        first = second
        second = ans
    }
    return second
}
fun isValid(code:Int,len:Int):Boolean{
    return if (len == 1){
       return code in 1..26
    }else{
        return code in 10 .. 26
    }
}

fun main() {
    println(numDecodings("12"))
}