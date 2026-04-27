class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s,t):
            if len(s) != len(t):
                return False
            else:
                sCount = {}
                for c in s:
                    if c not in sCount:
                        sCount[c] = 1
                    else:
                        sCount[c] += 1
                            
                tCount = {}
                for c in t:
                    if c not in tCount:
                        tCount[c] = 1
                    else:
                        tCount[c] += 1
                if sCount == tCount:
                    return True
        final = []
        used = []
        for i in range(len(strs)):
            if i not in used:
                sub = []
                sub.append(strs[i])
                used.append(i)
                r = i + 1
                while r < len(strs):
                    if r not in used:
                        if isAnagram(strs[i],strs[r]) is True:
                            sub.append(strs[r])
                            used.append(r)
                    r += 1
                if sub not in final:
                    final.append(sub)
        return final

            




