package leetcode

fun minOperations(boxes: String): IntArray {

    //Optimized Solution
    val result= IntArray(size = boxes.length)
    val n=boxes.length
    var count=0
    var total=0

    for (i in 0 ..< n){
        total+=count
        result[i] = total
        if (boxes[i] == '1'){
            count++
        }
    }

    total=0
    count=0

    for (i in n-1 downTo 0){
        total+=count
        result[i] += total
        if (boxes[i] == '1'){
            count++
        }
    }

    return result

    //Normal Solution
/*    val result= mutableListOf<Int>()
    for (i in boxes.indices){
        var count=0
        for (j in boxes.indices){
            if (boxes[j]=='1'){
                count+= Math.abs(i-j)
            }
        }
        result.add(count)
    }

    return result.toIntArray()*/

}

fun main() {
    println(minOperations("110").joinToString())
}