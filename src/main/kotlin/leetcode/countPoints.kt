package leetcode

fun countPoints(points: Array<IntArray>, queries: Array<IntArray>): IntArray {
    val list= mutableListOf<Int>()
    for (i in queries.indices){
        var count=0
        for (j in points.indices){
            val distance=Math.pow((points[j][0]-queries[i][0]).toDouble(), 2.0)+Math.pow((points[j][1]-queries[i][1]).toDouble(), 2.0)
            if (distance <= queries[i][2]*queries[i][2]){
                count+=1
            }
        }
        list.add(count)
    }
    return list.toIntArray()
}


fun main() {
    println(countPoints(
        points=arrayOf(intArrayOf(1,3), intArrayOf(3,3), intArrayOf(5,3), intArrayOf(2,2)),
        queries=arrayOf(intArrayOf(2,3,1), intArrayOf(4,3,1), intArrayOf(1,1,2))
    ).joinToString()
    )
}