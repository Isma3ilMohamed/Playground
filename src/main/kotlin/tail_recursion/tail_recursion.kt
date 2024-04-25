package tail_recursion

fun recursiveFactorial(n: Long) : Long {
    return if (n <= 1) {
        n
    } else {
        n * recursiveFactorial(n - 1)
    }
}

tailrec fun factorial(n:Long,accum:Long=1):Long{
    val soFar = n * accum
    return if (n <= 1) {
        soFar
    } else {
        factorial(n - 1, soFar)
    }
}
fun main() {
    println(factorial(5L))
}