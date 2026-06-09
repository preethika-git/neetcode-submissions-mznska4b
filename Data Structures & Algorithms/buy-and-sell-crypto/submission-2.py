class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p, maxP = prices, 0   
        l, r = 0, 1

        while r < len(p):
            if p[l] > p[r]:
                l = r
            else:
                maxP = max(maxP, p[r]-p[l])
            r+=1
        
        return maxP