class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        res = float('inf')
        sumArr = 0
        l = 0
        for r in range(len(nums)):
            sumArr += nums[r]
            while sumArr >= target:
                res = min(res, r - l + 1)
                sumArr -= nums[l]
                l += 1

        return int(res) if res != float('inf') else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
