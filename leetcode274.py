class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        for i, v in enumerate(citations):
            if len(citations) - i <= v:
                return len(citations) - i
        return 0


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([1, 3, 1]))
