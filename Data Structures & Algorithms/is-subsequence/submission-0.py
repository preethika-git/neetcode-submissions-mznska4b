class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ""
        for sc in s:
            for tc in t:
                if sc == tc:
                    res += tc
                    _, t = t.split(tc,1)
                    break
                else:
                    continue
        return True if res == s else False   


