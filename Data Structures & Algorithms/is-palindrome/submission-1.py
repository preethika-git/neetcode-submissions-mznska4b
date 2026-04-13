class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i].isalnum() == False:
                s = s.replace(s[i]," ")
        s = s.replace(" ","").lower()
        i = 0
        val = True
        while i < len(s)/2:
            if s[i] == s[-i-1]:
                i += 1
                continue
            else:
                val = False
                break
        return val

            