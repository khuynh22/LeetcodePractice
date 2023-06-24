class Solution:
    def search(self, nums, target):
        #     return self.binarySearch(nums, target)
        # def binarySearch(self, nums, target):
        #     l, r = 0, len(nums) - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if nums[mid] == target:
        #             return mid

        #         if nums[l] <= nums[mid]:
        #             if nums[mid] < target or target < nums[l]:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #         else:
        #             if nums[mid] > target or target > nums[r]:
        #                 r = mid - 1
        #             else:
        #                 l = mid + 1
        #     return -1
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

            def search(left, right):
                """
                Binary search
                """
                while left <= right:
                    pivot = (left + right) // 2
                    if nums[pivot] == target:
                        return pivot
                    else:
                        if target < nums[pivot]:
                            right = pivot - 1
                        else:
                            left = pivot + 1
                return -1

            n = len(nums)

            if n == 1:
                return 0 if nums[0] == target else -1

            rotate_index = find_rotate_index(0, n - 1)

            # if target is the smallest element
            if nums[rotate_index] == target:
                return rotate_index
            # if array is not rotated, search in the entire array
            if rotate_index == 0:
                return search(0, n - 1)
            if target < nums[0]:
                # search on the right side
                return search(rotate_index, n - 1)
            # search on the left side
            return search(0, rotate_index)


s = Solution()
print([4, 5, 6, 7, 0, 1, 2], 0)
print([4, 5, 6, 7, 0, 1, 2], 3)
print([1], 0)
