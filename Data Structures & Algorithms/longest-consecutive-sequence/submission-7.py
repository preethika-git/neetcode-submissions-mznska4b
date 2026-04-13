class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            nums.sort()
            cons = []
            con = 1
            cons.append(con)
            i = 0
            while i <= len(nums)-2:
                if nums[i] +1 == nums[i+1]:
                    con += 1
                    cons.append(con)
                    i += 1
                elif nums[i] == nums[i+1]:
                    i += 1  
                else:
                    cons.append(con)
                    con = 1
                    i += 1
                    
            return max(cons)
            



