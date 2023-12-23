package leetcode

fun isPathCrossing(path: String): Boolean {
    val originalMoves= mutableMapOf<Char,Pair<Int,Int>>()

    originalMoves['N'] = Pair(0,1)
    originalMoves['S'] = Pair(0,-1)
    originalMoves['W'] = Pair(-1,0)
    originalMoves['E'] = Pair(1,0)


    val visitedLocations= mutableSetOf<Pair<Int,Int>>()
    visitedLocations.add(Pair(0,0))


    var x=0
    var y=0
    for (c in path){
        val cur= originalMoves[c]
        val dx=cur!!.first
        val dy=cur!!.second

        x+=dx
        y+=dy
        val  curPair=Pair(x,y)
        if (visitedLocations.contains(curPair)){
            return true
        }
        visitedLocations.add(curPair)
    }


    return false
}


fun main() {
    println(isPathCrossing("SS"))
}