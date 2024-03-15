class Solution:
    def productExceptSelf(self, nums:List[int])->List[int]:
        prod_l=[1]*len(nums)
        n=len(nums)
        r=1
        
        for i in range(1,n):
            prod_l[i]=prod_l[i-1]*nums[i-1]
        for j in range(n-1,-1,-1):
            prod_l[j]=prod_l[j]*r
            r=r*nums[j]
            
        return prod_l
       
