class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            getIndex = self.binarySearch(
                numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if getIndex != -1:
                return [i + 1, getIndex + 1]
        return [-1, -1]

    def binarySearch(self, arr, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
