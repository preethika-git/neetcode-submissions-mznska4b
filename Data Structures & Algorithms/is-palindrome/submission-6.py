class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while r>l:
            if s[r].lower() == s[l].lower():
                r-=1
                l+=1
            elif not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                return False
        return True
