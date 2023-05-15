class Solution:
    def runningSum(self, nums):
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums
    
s = Solution()
print(s.runningSum([1,2,3,4]))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))