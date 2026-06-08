class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for l in range(len(nums)-1):
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append(l)
                    ans.append(r)
                r-=1

        return ans

