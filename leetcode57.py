class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        ans = []
        intervals.sort()
        i = 0
        temp = intervals[i]
        while i < len(intervals) - 1:
            if intervals[i + 1][0] <= temp[1]:
                if intervals[i + 1][1] <= temp[1]:
                    i += 1
                    continue
                else:
                    temp[1] = intervals[i + 1][1]
            else:
                ans.append(temp)
                temp = intervals[i + 1]
            i += 1

        ans.append(temp)
        return ans


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
