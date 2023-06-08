class Solution:
    import math
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1

            if res[nums[i]] > math.floor(len(nums) / 2):
                return nums[i]
            

