package dp

/*Top Down solution using recursion  "memoization"*/
fun climbingStairsTopDown(stairsNum: Int): Int {
    val map = HashMap<Int, Int>()

    fun countWays(n: Int): Int {
        if (n <= 1) return 1
        if (map.containsKey(n)) return map[n] ?: 1
        map[n] = countWays(n - 1) + countWays(n - 2)
        return map[n] ?: 1
    }

    return countWays(stairsNum)
}

/*Bottom up "Tabulation"*/
fun climbingStairsBottomUp(stairsNum: Int):Int{
    val array= IntArray(stairsNum+1){ 0 }
    array[0]=1
    array[1]=1

    for (i in 2..<array.size){
        array[i]=array[i-1] + array[i-2]
    }
    return array[stairsNum]
}


fun main() {
    println(climbingStairsBottomUp(5))
}