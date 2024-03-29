package grokking.two_pointers;

public class ValidPalindrome {

    public static boolean isPalindrome(String s){
        int left=0;
        int right =s.length()-1;

        while (left<=right){
            if (s.charAt(left) != s.charAt(right)){
                return false;
            }else{
                left++;
                right--;
            }
        }

        return true;
    }


    public static void main(String[] args) {
        System.out.println(isPalindrome("abba"));
    }
}
