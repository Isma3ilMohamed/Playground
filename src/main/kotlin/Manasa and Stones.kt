fun stones(n: Int, a: Int, b: Int): Array<Int> {
    val result: MutableList<Int> = ArrayList()
    val minAB = Math.min(a, b)
    val maxAB = Math.max(a, b)
    var i = minAB * (n - 1)
    while (i < maxAB * (n - 1)) {
        result.add(i)
        i += Math.abs(b - a)
    }
    result.add(maxAB * (n - 1))
    return result.toTypedArray()
}

fun main(args: Array<String>) {
    val T = readLine()!!.trim().toInt()

    for (TItr in 1..T) {
        val n = readLine()!!.trim().toInt()

        val a = readLine()!!.trim().toInt()

        val b = readLine()!!.trim().toInt()

        val result = stones(n, a, b)

        println(result!!.joinToString(" "))
    }
}