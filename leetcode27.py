class Solution:
    def removeElement(self, nums, val: int) -> int:
        size = 0
        for i in range(len(nums)):
            if nums[i] == val:
                size += 1
                nums[i] = 999

        nums.sort()
        return len(nums) - size


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
