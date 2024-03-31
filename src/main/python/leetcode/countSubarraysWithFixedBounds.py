class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans,mn,mx,last=0,-1,-1,-1
        for i in range(0,len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                mn=-1
                mx=-1
                last=i 
            if nums[i]==minK:
                mn=i 
            if nums[i]==maxK:
                mx=i 
            if mn!=-1 and mx!=-1:
                ans+=min(mx,mn)-last 
        return ans       
