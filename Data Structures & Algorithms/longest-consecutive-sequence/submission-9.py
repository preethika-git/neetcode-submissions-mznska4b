class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        cur_len = 0
        max_len = 0
        for x in s:
            if x-1 not in s:
                cur_len = 1
                while x+1 in s:
                    x += 1
                    cur_len += 1
                max_len = max(max_len,cur_len)
            
        return max_len

