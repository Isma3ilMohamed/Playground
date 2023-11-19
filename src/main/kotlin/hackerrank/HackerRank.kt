package hackerrank

//designerPdfViewer
val map= hashMapOf<Char,Int>().apply {
    ('a'..'z').forEachIndexed { index, c ->
        set(c,index)
    }
}
fun designerPdfViewer(h: Array<Int>, word: String): Int {
    // Write your code here
    var height=0
    word.forEach {
        if (height<h[map[it]!!])
            height=h[map[it]!!]
    }

    return height*word.count()
}

//encryption
fun transposeMatrix(matrix: MutableList<MutableList<String>>): Array<Array<String>> {
    val rows = matrix.size
    val cols = matrix[0].size

    // Create a new matrix with swapped rows and columns
    val transposedMatrix = Array(cols) { Array(rows) { "" } }

    for (i in 0 until rows) {
        for (j in 0 until cols) {
            transposedMatrix[j][i] = matrix[i][j]
        }
    }

    return transposedMatrix
}
fun encryption(s: String): String {
    // Write your code here
    var row= Math.floor(Math.sqrt(s.length.toDouble())).toInt()
    val col= Math.ceil(Math.sqrt(s.length.toDouble())).toInt()

    if (row*col<s.length){
        row+=1
    }
    var pivot=0
    val arr= MutableList(row){
        MutableList(col){
            ""
        }
    }
    for (i in arr.indices){
        for (j in arr[i].indices){
            arr[i][j] = s.getOrElse(pivot){ ' ' }.toString()
            pivot+=1
        }
    }

   val result= transposeMatrix(arr).map {
       it.joinToString("").trim()
   }.joinToString(" ")
    return result
}

fun main(args: Array<String>) {

    val s = readln()

    val result = encryption(s)

    println(result)
}
