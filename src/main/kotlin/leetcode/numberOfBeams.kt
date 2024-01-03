package leetcode

fun numberOfBeams(bank: Array<String>): Int {
    var prev=bank[0].count { it=='1' }
    var result=0

    for (i in 1 ..< bank.size){
        val curr=bank[i].count { it=='1' }
        if (curr>0){
            result += (prev*curr)
            prev = curr
        }
    }

    return result

}

fun main() {
    println(numberOfBeams(arrayOf("000","111","000",)))
}