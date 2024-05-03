class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        n1=len(arr1)
        n2=len(arr2)
        n = max(n1,n2)
        for i in range(n):
            v1 = int(arr1[i]) if i < len(arr1) else 0
            v2 = int(arr2[i]) if i < len(arr2) else 0
            
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0
        
        
