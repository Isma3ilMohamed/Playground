class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        I = len(nums1)
        J = len(nums2)
        res = []
        while i < I or j < J:
            cur_id = cur_val = 0
            if i < I and j < J:
                if nums1[i][0] < nums2[j][0]:
                    cur_id, cur_val = nums1[i]
                    i += 1
                elif nums1[i][0] > nums2[j][0]:
                    cur_id, cur_val = nums2[j]
                    j += 1
                elif nums1[i][0] == nums2[j][0]:
                    cur_id = nums1[i][0]
                    cur_val = nums1[i][1] + nums2[j][1]
                    i += 1
                    j += 1
            elif i < I:
                cur_id, cur_val = nums1[i]
                i += 1
            else:
                cur_id, cur_val = nums2[j]
                j += 1
            if not res or res and res[-1][0] != cur_id:
                res.append([cur_id, cur_val])
            else:
                res[-1][1] += cur_val
        return res
