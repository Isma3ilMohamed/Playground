package leetcode

private val sameDigitNumbers = listOf("999", "888", "777", "666", "555", "444", "333", "222", "111", "000")

// Check whether the 'num' string contains the 'sameDigitNumber' string or not.
private fun contains(sameDigitNumber: String, num: String): Boolean {
    for (index in 0..num.length - 3) {
        if (num[index] == sameDigitNumber[0] && num[index + 1] == sameDigitNumber[1] && num[index + 2] == sameDigitNumber[2]) {
            return true
        }
    }
    return false
}

fun largestGoodInteger(num: String): String? {
    // Iterate on all 'sameDigitNumbers' and check if the string 'num' contains it.
    for (sameDigitNumber in sameDigitNumbers) {
        if (contains(sameDigitNumber, num)) {
            // Return the current 'sameDigitNumbers'.
            return sameDigitNumber
        }
    }
    // No 3 consecutive same digits are present in the string 'num'.
    return ""
}