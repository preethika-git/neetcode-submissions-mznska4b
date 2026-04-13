class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_p = 0
        

        for l in range(n):
            r = n-1
            while l < r:
                while prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    max_p = max(max_p, profit)
                    r -= 1
                r -= 1
        
        return max_p

