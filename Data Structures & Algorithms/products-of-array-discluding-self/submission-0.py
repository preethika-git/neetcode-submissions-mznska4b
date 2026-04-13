class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            product = 1
            for i in range(len(nums)):
                if nums.index(num) != i:
                    product *= nums[i]
            output.append(product)
        return output
