class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid + 1] >= nums[mid]: 
                l = mid + 1
            else:
                r = mid
        
        return l

s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1]))