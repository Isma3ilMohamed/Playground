class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],x[1]))
        n = len(points)
        x,y = points[0]
        count=n

        for i in range(1,n):
            if x <= points[i][0] <= y:
                x=max(x,points[i][0])
                y = min(y,points[i][1])
                count -=1
            else:
                x = points[i][0]
                y = points[i][1]
        return count
