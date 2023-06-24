class Solution:
    def candy(self, ratings) -> int:
        resArr = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                resArr[i] = resArr[i - 1] + 1

        for i in range(len(ratings) - 1, 0, - 1):
            if ratings[i-1] > ratings[i]:
                resArr[i-1] = max(resArr[i-1], resArr[i]+1)
        return sum(resArr)


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
print(s.candy([1, 3, 2, 2, 1]))
print(s.candy([1, 2, 87, 87, 87, 2, 1]))
