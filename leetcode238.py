class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        res = [1] * len(nums)
        allProd = prod(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] *= int(allProd / nums[i])
            else:
                res[i] *= prod(nums[:i]) * prod(nums[i + 1:])
        

        return res
        