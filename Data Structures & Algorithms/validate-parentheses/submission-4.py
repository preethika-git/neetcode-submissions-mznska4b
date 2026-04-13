class Solution:
    def isValid(self, s: str) -> bool:
        br = {")":"(","}":"{","]":"["}
        stk = []
        for i in s:
            if i not in br:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != br[i]:
                        return False
                
        return not stk

                