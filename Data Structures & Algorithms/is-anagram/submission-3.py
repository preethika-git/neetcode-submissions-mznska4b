class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            ss = []
            for i in range(len(s)):
                char = s[i]
                ss.append(char)
            tt = []
            for i in range(len(t)):
                char = t[i]
                tt.append(char)
            tt.sort()
            ss.sort()
            if ss == tt: 
                return True 
            else:
                return False


