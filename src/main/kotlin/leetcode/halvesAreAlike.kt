package leetcode

fun halvesAreAlike(s: String): Boolean {
    val vowels: MutableSet<Char> = HashSet<Char>().apply {
        add('a')
        add('e')
        add('i')
        add('o')
        add('u')
        add('A')
        add('E')
        add('I')
        add('O')
        add('U')
    }

    val length = s.length
    val midPoint = length / 2
    val firstHalf = s.substring(0, midPoint)
    val secondHalf = s.substring(midPoint)
    return countVowels(firstHalf, vowels) == countVowels(secondHalf, vowels)
}

private fun countVowels(str: String, vowels: Set<Char>): Int {
    var count = 0
    for (c in str.toCharArray()) {
        if (vowels.contains(c)) {
            count++
        }
    }
    return count
}

fun main() {
    println(halvesAreAlike("book"))
}