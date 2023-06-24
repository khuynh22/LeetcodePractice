class Solution:
    def jump(self, nums) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            l = r + 1
            r = furthest
            res += 1
        return res


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
