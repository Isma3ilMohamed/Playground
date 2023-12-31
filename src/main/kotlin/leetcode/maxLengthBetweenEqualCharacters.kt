package leetcode

fun maxLengthBetweenEqualCharacters(s: String): Int {
    val firstIndex= HashMap<Char,Int>()
    var result=-1
    for(i in s.indices){
        if(firstIndex.containsKey(s[i])){
            result= result.coerceAtLeast(i - firstIndex[s[i]]!! - 1)
        }else{
            firstIndex[s[i]] = i
        }
    }
    return result
}

fun main() {
    println(maxLengthBetweenEqualCharacters("abca"))
}