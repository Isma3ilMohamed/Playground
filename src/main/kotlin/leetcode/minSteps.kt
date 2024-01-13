package leetcode

fun minSteps(s: String, t: String): Int {
    /*val count=IntArray(26)

    for (i in s.indices){
        count[t[i] - 'a']++
        count[s[i] - 'a']--
    }

    var ans=0
    for (i in 0..<26){
        ans += Math.max(0,count[i])
    }

    return ans*/
    var res=0
    for (c in t.toSet()){
        val diff=t.count { it==c } - s.count { it==c }
        res+= if (diff>0) diff else 0
    }
    return res
}

fun main() {
    println(minSteps("leetcode","practice"))
}