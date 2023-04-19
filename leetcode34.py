class Solution:
    def searchRange(self, nums, target):
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        return [l, r]

    def binarySearch(self, nums, target, leftMost):
        l, r = 0, len(nums) - 1
        i = -1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                i = mid
                if leftMost:
                    l = 0
                    r = mid - 1
                else:
                    l = mid + 1
                    r = len(nums) - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return i
    
# Test cases:
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([], 0))