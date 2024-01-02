package leetcode

fun findMatrix(nums: IntArray): List<List<Int>> {
    val map = HashMap<Int, Int>()
    val result = mutableListOf<MutableList<Int>>()
    nums.forEach {
        val row=map.getOrDefault(it,0)
        if (result.size==row){
            result.add(mutableListOf())
        }
        result[row].add(it)
        if (map.containsKey(it)){
            map[it] = map.get(it)!! + 1
        }else{
            map.put(it,1)
        }
    }
    return result
}


fun main() {
    println(findMatrix(intArrayOf(1,3,4,1,2,3,1)))
}