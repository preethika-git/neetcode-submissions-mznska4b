class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p, l, maxP = prices, 0, 0

        for l in range(len(p)-1):
            r = len(p)-1
            
            while r > l:
                if p[r] > p[l]:
                    profit = p[r] - p[l]
                    maxP = max(profit, maxP)
                r -= 1

        return maxP       