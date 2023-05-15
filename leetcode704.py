class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
    
s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))