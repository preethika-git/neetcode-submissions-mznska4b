class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stk = []

        for i in s:
            if i in key.keys():
                stk.append(i)
            elif len(stk) != 0 and i == key[stk[-1]]:
                stk.pop()
            else:
                return False
        
        return True if len(stk) == 0 else False


