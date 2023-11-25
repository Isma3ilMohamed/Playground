package leetcode

fun getSumAbsoluteDifferences(nums: IntArray): IntArray {
    val n=nums.size
    val ans = IntArray(n)
    val total = nums.sum()
    var leftSum=0
    for (i in 0..<n){
        val rightSum=total-leftSum-nums[i]
        val rightCount=n-1-i

        val leftTotal = i * nums[i] - leftSum
        val rightTotal=rightSum-rightCount * nums[i]

        ans[i]=leftTotal+rightTotal
        leftSum+=nums[i]
    }

    return ans
}

fun main() {
    println(getSumAbsoluteDifferences(intArrayOf(2,3,5)).joinToString())
}