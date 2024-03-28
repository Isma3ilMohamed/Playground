package grokking.two_pointers;

public class ValidPalindrome2 {

    public static boolean isPalindrome(String s,int left,int right){
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

    public static boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (start <= end) {
            if (s.charAt(start) != s.charAt(end)) {
                //check if it's palindrome after remove start and end char
                return isPalindrome(s,start+1,end) || isPalindrome(s,start,end-1);

            } else {
                start++;
                end--;
            }
        }
        return true;
    }


    public static void main(String[] args) {
        System.out.println(isPalindrome("eeccccbebaeeabebccceea"));
    }
}
