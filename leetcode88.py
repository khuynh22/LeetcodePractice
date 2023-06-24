class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()


s = Solution()
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))
