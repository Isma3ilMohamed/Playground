class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        totalSum =( n * (n+1) // 2)

        while(left < right):
            mid = (left+right) // 2

            if((mid * mid) - totalSum < 0):
                left = mid+1
            else:
                right = mid
        
        if((left*left) - totalSum == 0):
            return left
        else:
            return -1
