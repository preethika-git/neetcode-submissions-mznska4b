class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count2 = {}

        if len(s) != len(t):
            return False
        
        else:
            for i in s:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
            for i in t:
                if i not in count2:
                    count2[i] = 1
                else:
                    count2[i] += 1
            if count ==  count2:
                return True
            else:
                return False