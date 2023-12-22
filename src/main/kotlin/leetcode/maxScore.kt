package leetcode

fun maxScore(s: String): Int {
    var ones=0
    for (i in s.indices){
        if (s[i] == '1'){
            ones+=1
        }
    }
    var ans=0
    var zeros=0
    for (i in 0..< s.length-1){
        if (s[i]=='1'){
            ones-=1
        }else{
            zeros+=1
        }

        ans=Math.max(ans,zeros+ones)
    }

    return ans

}


fun main() {
    println(maxScore("011101"))
}