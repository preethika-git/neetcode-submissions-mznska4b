class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        ans=[]

        for l in range(len(nums)):
            r = len(nums)-1
            while r>l:
                if nums[l] + nums[r] == target:
                    ans.append(l)
                    ans.append(r)
                    break
                else:
                    r -= 1
        return ans
        
                    