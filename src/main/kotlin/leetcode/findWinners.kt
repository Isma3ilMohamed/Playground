package leetcode


fun findWinners(matches: Array<IntArray>): List<List<Int>>? {
    val losses = IntArray(100001)
    for (i in matches.indices) {
        val win = matches[i][0]
        val loss = matches[i][1]
        if (losses[win] == 0) {
            losses[win] = -1
        }
        if (losses[loss] == -1) {
            losses[loss] = 1
        } else {
            losses[loss]++
        }
    }
    val zeroLoss: MutableList<Int> = ArrayList()
    val oneLoss: MutableList<Int> = ArrayList()
    val result: MutableList<List<Int>> = ArrayList()
    for (i in losses.indices) {
        if (losses[i] == -1) {
            zeroLoss.add(i)
        } else if (losses[i] == 1) {
            oneLoss.add(i)
        }
    }
    result.add(zeroLoss)
    result.add(oneLoss)
    return result
}