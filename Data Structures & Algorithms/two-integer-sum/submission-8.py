from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = defaultdict(int)

        for idx, num in enumerate(nums):
            d = target - num
            if d in key:
                return [key[d], idx]
            key[num] = idx


