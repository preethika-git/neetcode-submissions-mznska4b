class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = []
        for c in nums:
            if c not in count:
                count.append(c)
                continue
            else:
                return True
        return False

        