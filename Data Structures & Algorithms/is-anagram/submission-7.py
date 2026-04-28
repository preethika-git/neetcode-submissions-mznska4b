class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        else:
            count = defaultdict(int)
            for c in s:
                count[c] += 1
            for c in t:
                count[c] -= 1
            for v in count.values():
                if v != 0:
                    return False
            return True