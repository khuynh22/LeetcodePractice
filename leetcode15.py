class Solution:
    def threeSum(self, nums):
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        nums.sort()
        res = []
        i = 0
        while nums[i] <= 0 and i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if -nums[i] == nums[l] + nums[r]:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif -nums[i] < nums[l] + nums[r]:
                        r -= 1
                    else:
                        l += 1
            i += 1
        return res
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))