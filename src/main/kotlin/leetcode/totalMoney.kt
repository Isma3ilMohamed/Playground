package leetcode

fun totalMoney(n: Int): Int {
   return (1..n).sumOf {
        (it-1)%7 + 1 + (it-1)/7
    }

}

fun main() {
    println(totalMoney(10))
}