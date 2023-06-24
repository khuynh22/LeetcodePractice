class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)

        count = 0
        slow = 0
        fast = 2
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                fast += 1
                slow = fast - 2
            else:
                nums[fast] = 999
                count += 1
                fast += 1

        nums.sort()
        return len(nums) - count
