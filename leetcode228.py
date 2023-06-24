class Solution:
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        temp = [nums[0], nums[0]]
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                temp[1] = nums[i + 1]
            else:
                if temp[0] == temp[1]:
                    res.append(str(temp[0]))
                else:
                    res.append(str(temp[0]) + "->" + str(temp[1]))
                temp = [nums[i + 1], nums[i + 1]]
        if temp[0] == temp[1]:
            res.append(str(temp[0]))
        else:
            res.append(str(temp[0]) + "->" + str(temp[1]))
        return res


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
print(s.summaryRanges([]))
