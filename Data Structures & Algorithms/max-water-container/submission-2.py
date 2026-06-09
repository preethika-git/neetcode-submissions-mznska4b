class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r, l = len(heights)-1, 0
        max_vol = 0

        while r > l:
            h = min(heights[l],heights[r])
            w = r - l
            vol_new = h*w

            max_vol = max(max_vol,vol_new)

            if heights[l] < heights[r]:
                l += 1  
            else:
                r -= 1

        return max_vol      