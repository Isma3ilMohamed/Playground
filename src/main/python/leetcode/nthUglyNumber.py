class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Array to store the first n ugly numbers
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1  # The first ugly number is 1

        # Pointers for multiples of 2, 3, and 5
        i2, i3, i5 = 0, 0, 0

        # Initial multiples of 2, 3, and 5
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            # Choose the smallest next multiple
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly_numbers[i] = next_ugly

            # Increment the pointer(s) that matched the smallest value
            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly_numbers[i2] * 2
            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly_numbers[i3] * 3
            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly_numbers[i5] * 5

        return ugly_numbers[-1]
