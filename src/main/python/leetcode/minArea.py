from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left = self.searchColumns(image, 0, y, 0, m, True)
        right = self.searchColumns(image, y + 1, n, 0, m, False)
        top = self.searchRows(image, 0, x, left, right, True)
        bottom = self.searchRows(image, x + 1, m, left, right, False)
        return (right - left) * (bottom - top)
    
    def searchColumns(self, image: List[List[str]], i: int, j: int, top: int, bottom: int, whiteToBlack: bool) -> int:
        while i != j:
            k, mid = top, (i + j) // 2
            while k < bottom and image[k][mid] == '0':
                k += 1
            if (k < bottom) == whiteToBlack:
                j = mid  # search the boundary in the smaller half
            else:
                i = mid + 1  # search the boundary in the greater half
        return i
    
    def searchRows(self, image: List[List[str]], i: int, j: int, left: int, right: int, whiteToBlack: bool) -> int:
        while i != j:
            k, mid = left, (i + j) // 2
            while k < right and image[mid][k] == '0':
                k += 1
            if (k < right) == whiteToBlack:
                j = mid
            else:
                i = mid + 1
        return i
