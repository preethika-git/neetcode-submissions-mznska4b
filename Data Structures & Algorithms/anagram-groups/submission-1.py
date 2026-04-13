class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        def isAnagram(x,y):
            xx = Counter(x)
            yy = Counter(y)
            if xx == yy:
                return True
            else:
                return False
        
        lst = []
        strs_new = strs.copy()
        for i in range(len(strs)):
            if strs[i] in strs_new:    
                anagrams = [strs[i]]
                strs_new.remove(strs[i])
                for j in range(len(strs)):
                    if i < j:    
                        if isAnagram(strs[i],strs[j]) == True:
                            strs_new.remove(strs[j])
                            anagrams.append(strs[j])
                lst.append(anagrams)

        return lst
                


            




