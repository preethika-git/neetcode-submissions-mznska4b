class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL, l = 0, 0
        for i in nums:
            if i == 1:
                l+=1
                maxL = max(maxL,l)
            else:
                l=0
        return maxL
