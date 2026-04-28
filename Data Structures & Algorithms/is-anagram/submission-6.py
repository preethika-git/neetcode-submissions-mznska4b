class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            ss = tuple(sorted(s))
            tt = tuple(sorted(t))
            if ss == tt:
                return True
            else:
                return False   