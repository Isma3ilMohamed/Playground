class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        totalsum,hashmap=0,{0:-1}
        res,diff=0,0
        for i in range(len(nums)):
            if(nums[i]==0):
                totalsum-=1
            else:
                totalsum+=1
            try:
                diff=i-hashmap[totalsum]
                if(diff>res):
                    res=diff
            except:
                hashmap[totalsum]=i
        return res
        
