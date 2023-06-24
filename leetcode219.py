class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict and abs(i - numDict[nums[i]] <= k):
                return True
            numDict[nums[i]] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(s.containsNearbyDuplicate([99, 99], 2))
print(s.containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3))
