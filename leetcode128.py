class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 0
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] == nums[i] + 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
            
        res = max(res, temp)
        return res
    
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([]))
print(s.longestConsecutive([0,1,1,2]))