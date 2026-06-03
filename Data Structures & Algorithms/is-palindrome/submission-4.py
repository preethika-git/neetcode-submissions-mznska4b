class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1
        l = 0
        ans = True
        while r>l:
            if s[r].isalnum() == True:
                if s[l].isalnum() == True:
                    if s[r].lower() != s[l].lower():
                        ans = False
                        break
                    else:
                        r-=1
                        l+=1
                else: 
                    l+=1
            else:
                r-=1
        return ans