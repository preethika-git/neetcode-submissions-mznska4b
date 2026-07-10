class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.split(" ")
        
        i=-1
        
        while len((w[i])) == 0:
            i -= 1
        
        return len(w[i])