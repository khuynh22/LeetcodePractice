class Solution:
    def merge(self, intervals):
        ans = []
        intervals.sort()
        i = 0
        temp = intervals[i]
        while i < len(intervals) - 1:
            print(temp)
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
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
