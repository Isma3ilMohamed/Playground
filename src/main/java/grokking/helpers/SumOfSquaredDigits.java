package grokking.helpers;

// Helper function that calculates the sum of squared digits
public class SumOfSquaredDigits{
    public static int sumOfSquaredDigits(int number) {
        int totalSum = 0;
        while (number != 0) {
            int digit = number % 10;
            number = number / 10;
            totalSum += (int) Math.pow(digit, 2);
        }
        return totalSum;
    }
}