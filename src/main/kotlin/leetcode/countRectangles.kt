package leetcode

import java.util.*
import kotlin.collections.ArrayList


/*
fun countRectangles(rectangles: Array<IntArray>, points: Array<IntArray>): IntArray {
    val result = mutableListOf<Int>()
    for (i in points.indices) {
        var count = 0
        for (j in rectangles.indices) {
            if (points[i][0] <= rectangles[j][0] && points[i][1] <= rectangles[j][1]) {
                count += 1
            }
        }
        result.add(count)
    }

    return result.toIntArray()
}

*/

fun countRectangles(rectangles: Array<IntArray>, points: Array<IntArray>): IntArray {
    val res = IntArray(points.size)
    // Create a map
    val map: MutableList<MutableList<Int>> = ArrayList(101)
    // add all the reactangle that ends at a particular height
    for (i in 0..100) {
        map.add(ArrayList())
    }
    for (rec in rectangles) {
        val l = rec[0]
        val h = rec[1]
        map[h].add(l)
    }
    // sort the x coordinates for each height
    for (i in 0..100) {
        map[i].sort()
    }
    for (i in points.indices) {
        var count = 0
        val x = points[i][0]
        val y = points[i][1]
        for (j in y..100) {
            val rectanglesEndingAtHeightJ: List<Int> = map[j]
            val index = binarySearch(rectanglesEndingAtHeightJ, x)
            count += rectanglesEndingAtHeightJ.size - index
        }
        res[i] = count
    }
    return res
}

private fun binarySearch(list: List<Int>, x: Int): Int {
    var left = 0
    var right = list.size
    while (left < right) {
        val mid = left + (right - left) / 2
        if (list[mid] >= x) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}


fun main() {
    println(
        countRectangles(
            rectangles = arrayOf(intArrayOf(1, 2), intArrayOf(2, 3), intArrayOf(2, 5)),
            points = arrayOf(intArrayOf(2, 1), intArrayOf(1, 4))
        ).joinToString()
    )
}