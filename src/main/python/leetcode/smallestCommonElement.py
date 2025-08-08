class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        commonList = mat[0]
        for lists in mat:
            commonList = self.intersection(commonList,lists)
        
        if(commonList):
            return commonList[0]
        return -1
    
    def intersection(self,list1: List[int], list2: List[int]) -> List[int]:
        return list(set(list1) & set(list2))
