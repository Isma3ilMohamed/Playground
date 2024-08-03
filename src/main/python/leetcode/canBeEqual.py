class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort()
        target.sort()

        for i in range(0,len(target)):
            if arr[i] != target[i]:
                return False
        
        return True
