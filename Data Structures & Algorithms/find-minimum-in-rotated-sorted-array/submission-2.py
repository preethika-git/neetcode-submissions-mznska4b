class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) -1 
        l = 0
        m = 0

        while l < r:
            m = (r+l)//2
            if m != l:
                if nums[l] < nums [r]:
                    if nums[m] < nums[l]:
                        l = m
                    else:
                        r = m
                else:
                    if nums[m] < nums[r]:
                        r = m
                    else:
                        l = m
            else:
                return min(nums[l],nums[r])
        return nums[l]







                    