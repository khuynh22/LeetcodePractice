class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while (l < r):
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17]))