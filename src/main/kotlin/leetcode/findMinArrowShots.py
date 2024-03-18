class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        arrow=1
        end=points[0][1]
        for point in points:
            if point[0] > end:
                end=point[1]
                arrow +=1

        return arrow




solution = Solution()

print(solution.findMinArrowShots(points=[[10,16],[2,8],[1,6],[7,12]]))