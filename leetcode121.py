class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minBuy = float('inf')

        for i in range(len(prices)):
            minBuy = min(prices[i], minBuy)
            maxPro = max(maxPro, prices[i] - minBuy)

        return maxPro
