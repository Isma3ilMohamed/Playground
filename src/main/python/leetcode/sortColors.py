class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r_cnt = 0
        w_cnt = 0
        b_cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                r_cnt += 1
            elif nums[i] == 1:
                w_cnt += 1
            else:
                b_cnt += 1
        
        nums[:r_cnt] = [0] * r_cnt
        nums[r_cnt:r_cnt+w_cnt] = [1] * w_cnt
        if b_cnt > 0:
            nums[-b_cnt:] = [2] * b_cnt

            
