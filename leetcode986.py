class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []

        res = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return res


s = Solution()
print([[0, 2], [5, 10], [13, 23], [24, 25]],
      [[1, 5], [8, 12], [15, 24], [25, 26]])
print([[1, 3], [5, 9]], [])
