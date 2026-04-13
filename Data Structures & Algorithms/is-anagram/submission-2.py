class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = []
        for l in range(len(s)):
            ss.append(s[l])
        ss.sort()    
        tt = []
        for l in range(len(t)):
            tt.append(t[l])
        tt.sort()
        if len(ss) == len(tt):
            for i in range(len(ss)):
                if ss[i] == tt[i]:
                    continue
                else:
                    return False
            return True 
        else:
            return False