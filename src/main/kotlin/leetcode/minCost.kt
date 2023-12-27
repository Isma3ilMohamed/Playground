package leetcode

fun minCost(colors: String, neededTime: IntArray): Int {
    var totalTime = 0
    var i=0
    var j=0
    while (i< neededTime.size){
        var currentTotal=0
        var currMax=0
        while(j<neededTime.size && colors[i] == colors[j]){
            currentTotal += neededTime[j]
            currMax = Math.max(currMax,neededTime[j])
            j+=1
        }
        totalTime += currentTotal - currMax
        i = j
    }
    return totalTime
}

fun main() {
   println( minCost(colors = "abc", neededTime = intArrayOf(1,2,3)))
}