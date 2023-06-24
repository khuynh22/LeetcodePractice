class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        for a in range(len(nums) - 1):
            if (nums[a] != nums[a + 1]):
                nums[i] = nums[a + 1]
                i += 1

        return i


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
