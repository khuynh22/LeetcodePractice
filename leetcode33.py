class Solution:
    def search(self, nums, target):
        return self.binarySearch(nums, target)
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
        return -1
    
s = Solution()
print([4,5,6,7,0,1,2], 0)
print([4,5,6,7,0,1,2], 3)
print([1], 0)
    