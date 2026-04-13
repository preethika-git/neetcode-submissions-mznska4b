class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        val = True
        while right > left:
            if s[left].isalnum() == True and s[right].isalnum() == True:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    val = False
                    break
            elif s[left].isalnum() != True:
                left += 1
                continue
            elif s[right].isalnum() != True:
                right -= 1
                continue
        return val
            