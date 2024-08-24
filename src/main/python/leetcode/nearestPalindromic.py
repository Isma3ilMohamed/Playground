class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        # Middle prefix to base the palindrome on
        prefix = int(n[:(length + 1) // 2])

        # Generate possible palindrome candidates
        candidates = set()
        # Case 1: Reflect the prefix
        candidates.add(self.make_palindrome(str(prefix), length % 2))
        # Case 2: Increment the prefix and reflect
        candidates.add(self.make_palindrome(str(prefix + 1), length % 2))
        # Case 3: Decrement the prefix and reflect
        candidates.add(self.make_palindrome(str(prefix - 1), length % 2))

        # Consider special cases like all 9's or all 0's
        candidates.add("9" * (length - 1))
        candidates.add("1" + "0" * (length - 1) + "1")

        candidates.discard(n)  # Exclude the original number itself

        # Find the closest palindrome
        def difference(x):
            return abs(int(x) - int(n))

        return min(candidates, key=lambda x: (difference(x), int(x)))

    def make_palindrome(self, half: str, odd_length: bool) -> str:
        if odd_length:
            return half + half[-2::-1]
        else:
            return half + half[::-1]
