class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key = lambda x: x[1])
        arrow, bound = 1, points[0][1]
        for start, end in points:
            if bound < start:
                bound = end
                arrow += 1
        return arrow

s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))