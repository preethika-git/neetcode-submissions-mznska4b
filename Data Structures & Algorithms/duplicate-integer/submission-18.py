class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for y in range(len(nums)-1):
                if nums[i] == nums[y+1] and i != y+1:
                    return True
                    break
                else:
                    continue
        return False