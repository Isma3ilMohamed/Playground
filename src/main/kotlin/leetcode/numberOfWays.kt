const val MOD = 1000000007

fun numberOfWays(corridor: String): Int {
    var zero = 0
    var one = 0
    var two = 1

    for (thing in corridor.toCharArray()) {
        if (thing == 'S') {
            zero = one
            val temp = one
            one = two
            two = temp
        } else {
            two = (two + zero) % MOD
        }
    }

    return zero
}

fun main() {
    println(numberOfWays("SSPPSPS"))
}