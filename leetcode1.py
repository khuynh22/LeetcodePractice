class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i


print([2, 7, 11, 15], 9)
print([3, 2, 4], 6)
print([3, 3], 6)
