class Solution:
    def maxArea(self, height) -> int:
        res = 0
        i, j = 0, len(height) - 1

        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return res
    

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))