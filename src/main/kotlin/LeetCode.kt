import java.util.*

fun isPalindrome(x: Int): Boolean {
    return x.toString() == x.toString().reversed()
}

fun minPairSum(nums: IntArray): Int {
    var max = 0
    Arrays.sort(nums)
    var firstPointer = 0
    var lastPointer = (nums.size) - 1
    while (firstPointer < nums.size / 2) {
        max = Math.max(max, nums[firstPointer] + nums[lastPointer])
        firstPointer++
        lastPointer--
    }
    return max
}

fun maxFrequency(nums: IntArray, k: Int): Int {
    Arrays.sort(nums)
    var i = 0
    var j = 0
    var sum = 0
    var maxLength = 0


    i = 0
    while (i < nums.size) {
        sum += nums[i]
        while ((i - j + 1) * nums[i] - sum > k) {
            sum -= nums[j]
            j++
        }
        maxLength = Math.max(maxLength, i - j + 1)
        i++
    }


    return maxLength
}

fun main() {
    println(maxFrequency(intArrayOf(1, 4, 8, 13), 5))
}