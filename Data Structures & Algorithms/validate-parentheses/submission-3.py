class Solution:
    def isValid(self, s: str) -> bool:
        br = {")":"(","}":"{","]":"["}
        stk = []
        for i in s:
            if i not in br:
                stk.append(i)
            elif len(stk) > 0:
                popped = stk.pop()
                if popped != br[i]:
                    return False
            else:
                return False
        return not stk

                