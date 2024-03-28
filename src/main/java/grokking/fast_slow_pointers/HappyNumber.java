package grokking.fast_slow_pointers;

import grokking.helpers.SumOfSquaredDigits;

public class HappyNumber {
    public static int sumOfSquaredDigits(int number) {
        int totalSum = 0;
        while (number != 0) {
            int digit = number % 10;
            number = number / 10;
            totalSum += (int) Math.pow(digit, 2);
        }
        return totalSum;
    }
    public static boolean isHappyNumber(int n) {

        int slow=n;
        int fast=sumOfSquaredDigits(n);

        while (fast!=1 && slow!=fast){
            slow=sumOfSquaredDigits(slow);
            fast=sumOfSquaredDigits(sumOfSquaredDigits(fast));
        }

        return fast==1;
    }

    public static void main(String[] args) {
        System.out.println(isHappyNumber(28));
    }
}
