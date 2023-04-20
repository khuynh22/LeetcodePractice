class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while (l <= r):
            mid = (l + r) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))